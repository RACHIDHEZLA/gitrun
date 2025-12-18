#!/usr/bin/env python3
"""
gitrun - تشغيل سكربتات بايثون مباشرة من GitHub/GitLab
"""
import os
import sys
import tempfile
import shutil
import subprocess
import requests
from typing import Optional, List, Dict, Tuple
from urllib.parse import urlparse
import venv
import platform

class GitRunner:
    """المحرك الرئيسي لتشغيل الكود من مستودعات Git"""
    
    SUPPORTED_PLATFORMS = {
        'github': {
            'raw_template': 'https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{path}',
            'api_template': 'https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={ref}'
        },
        'gitlab': {
            'raw_template': 'https://gitlab.com/{owner}/{repo}/-/raw/{ref}/{path}',
            'api_template': 'https://gitlab.com/api/v4/projects/{owner}%2F{repo}/repository/files/{path}?ref={ref}'
        }
    }
    
    def __init__(self, repo_url: str, branch: str = 'main', 
                 script: Optional[str] = None, verbose: bool = False,
                 use_venv: bool = True):
        self.repo_url = repo_url.rstrip('/')
        self.branch = branch
        self.script = script
        self.verbose = verbose
        self.use_venv = use_venv
        self.temp_dir = tempfile.mkdtemp(prefix='gitrun_')
        
        # تحليل URL
        self.platform, self.owner, self.repo = self._parse_repo_url()
        
        if self.verbose:
            print(f"🔍 تحليل الريبو: {self.owner}/{self.repo} على {self.platform}")
            print(f"📁 المجلد المؤقت: {self.temp_dir}")
    
    def _parse_repo_url(self) -> Tuple[str, str, str]:
        """تحليل رابط المستودع"""
        parsed = urlparse(self.repo_url)
        host = parsed.netloc.lower()
        path_parts = parsed.path.strip('/').split('/')
        
        # تحديد المنصة
        if 'github' in host:
            platform = 'github'
        elif 'gitlab' in host:
            platform = 'gitlab'
        else:
            raise ValueError(f"المنصة غير مدعومة: {host}. يدعم فقط GitHub و GitLab حالياً")
        
        # استخراج المالك والمستودع
        if len(path_parts) >= 2:
            owner = path_parts[0]
            repo = path_parts[1].replace('.git', '')
            return platform, owner, repo
        else:
            raise ValueError("رابط المستودع غير صحيح")
    
    def _get_raw_url(self, path: str = '') -> str:
        """إنشاء رابط للنسخة الخام من الملف"""
        template = self.SUPPORTED_PLATFORMS[self.platform]['raw_template']
        return template.format(
            owner=self.owner,
            repo=self.repo,
            ref=self.branch,
            path=path
        )
    
    def _fetch_file(self, filename: str) -> Optional[str]:
        """جلب محتوى ملف من المستودع"""
        url = self._get_raw_url(filename)
        if self.verbose:
            print(f"📥 جلب: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
            else:
                if self.verbose:
                    print(f"⚠️  ملف غير موجود: {filename} (HTTP {response.status_code})")
                return None
        except requests.RequestException as e:
            if self.verbose:
                print(f"⚠️  خطأ في جلب {filename}: {e}")
            return None
    
    def _setup_virtualenv(self) -> Tuple[str, str]:
        """إنشاء وإعداد بيئة افتراضية مؤقتة"""
        if not self.use_venv:
            return sys.executable, f"{sys.executable} -m pip"
        
        venv_dir = os.path.join(self.temp_dir, "venv")
        
        if self.verbose:
            print(f"🔧 إنشاء بيئة افتراضية في: {venv_dir}")
        
        # إنشاء virtual environment
        venv.create(venv_dir, with_pip=True)
        
        # تحديد مسار python و pip حسب نظام التشغيل
        if platform.system() == "Windows":
            python_path = os.path.join(venv_dir, "Scripts", "python.exe")
            pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
        else:
            python_path = os.path.join(venv_dir, "bin", "python")
            pip_path = os.path.join(venv_dir, "bin", "pip")
        
        return python_path, pip_path
    
    def install_requirements(self, python_path: str, pip_path: str):
        """تثبيت متطلبات المشروع"""
        content = self._fetch_file('requirements.txt')
        
        if content:
            req_path = os.path.join(self.temp_dir, 'requirements.txt')
            with open(req_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            if self.verbose:
                print("📦 تثبيت المتطلبات...")
                print(f"🔧 استخدام: {pip_path}")
            
            # تثبيت المتطلبات في الـ venv
            result = subprocess.run(
                [pip_path, "install", "-r", req_path],
                capture_output=not self.verbose,
                text=True,
                cwd=self.temp_dir
            )
            
            if result.returncode == 0:
                print("✅ تم تثبيت المتطلبات بنجاح")
            else:
                if self.verbose:
                    print(f"⚠️  هناك مشاكل في التثبيت: {result.stderr[:200]}...")
        else:
            if self.verbose:
                print("ℹ️  لا يوجد requirements.txt - تخطي تثبيت المتطلبات")
                
    def detect_main_script(self) -> str:
    """اكتشاف الملف الرئيسي تلقائياً"""
    # قائمة موسعة بالأسماء الشائعة
    common_scripts = [
        'main.py', 'app.py', 'run.py', 'cli.py',
        'index.py', 'script.py', 'start.py',
        'setup.py', 'manage.py', 'demo.py',  # أضفنا demo.py
        '__main__.py'
    ]
    
    # تحقق من الملفات الشائعة
    for script in common_scripts:
        if self._fetch_file(script) is not None:
            if self.verbose:
                print(f"🔍 عثرت على الملف الرئيسي: {script}")
            return script
    
    # إذا لم نجد ملفاً شائعاً، نبحث عن أي ملف .py في المجلد الجذر
    try:
        if self.platform == 'github':
            api_url = f'https://api.github.com/repos/{self.owner}/{self.repo}/contents?ref={self.branch}'
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200:
                files = response.json()
                # ترتيب الملفات: أولاً .py في الجذر، ثم في المجلدات
                py_files = []
                for f in files:
                    if f['name'].endswith('.py'):
                        if '/' not in f['path']:  # ملفات في الجذر أولاً
                            py_files.insert(0, f['name'])
                        else:
                            py_files.append(f['name'])
                
                if py_files:
                    if self.verbose:
                        print(f"🔍 وجدت ملفات بايثون: {py_files[:3]}...")
                    return py_files[0]
    except Exception as e:
        if self.verbose:
            print(f"⚠️  خطأ في البحث عبر API: {e}")
    
    # البحث في مجلدات معروفة
    for folder in ['src', 'app', 'project', 'micrograd']:
        for script_name in ['__init__.py', 'main.py']:
            potential_path = f"{folder}/{script_name}"
            if self._fetch_file(potential_path) is not None:
                if self.verbose:
                    print(f"🔍 عثرت على الملف في مجلد: {potential_path}")
                return potential_path
    
    # الافتراضي - ولكن هذه المرة مع رسالة أفضل
    if self.verbose:
        print("⚠️  لم أجد ملفاً رئيسياً واضحاً، جرب تحديده يدوياً باستخدام --script")
    return 'main.py'
    
    def run_script(self, python_path: str, user_args: List[str] = None):
        """تنزيل وتشغيل السكربت"""
        if user_args is None:
            user_args = []
        
        # تحديد اسم الملف
        script_name = self.script or self.detect_main_script()
        
        # جلب محتوى الملف
        content = self._fetch_file(script_name)
        if content is None:
            raise FileNotFoundError(f"لم أستطع العثور على الملف: {script_name}")
        
        # حفظ الملف مؤقتاً
        script_path = os.path.join(self.temp_dir, script_name)
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"🚀 تشغيل {script_name} من {self.owner}/{self.repo}")
        
        # تشغيل السكربت مع arguments المستخدم
        cmd = [python_path, script_path] + user_args
        
        if self.verbose:
            print(f"⚡ الأمر: {' '.join(cmd)}")
        
        try:
            subprocess.run(cmd, cwd=self.temp_dir, check=True)
        except subprocess.CalledProcessError as e:
            sys.exit(e.returncode)
    
    def cleanup(self):
        """تنظيف الملفات المؤقتة"""
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
            if self.verbose:
                print(f"🧹 تم تنظيف المجلد المؤقت")
    
    def run(self, user_args: List[str] = None):
        """الدالة الرئيسية لتشغيل كل شيء"""
        if user_args is None:
            user_args = []
        
        try:
            # 1. إعداد البيئة الافتراضية
            python_path, pip_path = self._setup_virtualenv()
            
            # 2. تثبيت المتطلبات
            self.install_requirements(python_path, pip_path)
            
            # 3. تشغيل السكربت
            self.run_script(python_path, user_args)
            
        except KeyboardInterrupt:
            print("\n⏹️  تم إيقاف التشغيل بواسطة المستخدم")
        except Exception as e:
            print(f"💥 خطأ: {e}", file=sys.stderr)
            sys.exit(1)
        finally:
            # 4. التنظيف
            self.cleanup()
