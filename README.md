# 🚀 gitrun

[![PyPI version](https://badge.fury.io/py/gitrun.svg)](https://badge.fury.io/py/gitrun)
[![Python versions](https://img.shields.io/pypi/pyversions/gitrun.svg)](https://pypi.org/project/gitrun/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/gitrun/month)](https://pepy.tech/project/gitrun)

**تشغيل سكربتات بايثون ودفاتر Jupyter مباشرة من GitHub أو GitLab — بدون تنزيل المستودع كاملاً!**  
مع بيئة افتراضية معزولة، اكتشاف ذكي للفرع والملف الرئيسي، وتنظيف تلقائي.

**Run Python scripts and Jupyter notebooks directly from GitHub or GitLab — without cloning the entire repo!**  
With isolated virtual environments, smart branch/file detection, and automatic cleanup.

---

## ✨ المميزات الرئيسية / Key Features

- ✅ **تشغيل فوري** بدون `git clone`  
  Instant execution without full repository download
- ✅ **بيئة افتراضية معزولة** (لا تؤثر على نظامك)  
  Isolated temporary virtual environment
- ✅ **دعم Jupyter notebooks** (يفتح `jupyter lab` تلقائيًا)  
  Full Jupyter notebook support (auto-launches JupyterLab)
- ✅ **اكتشاف ذكي للفرع الافتراضي** (main أو master أو أي اسم)  
  Smart default branch detection via GitHub API
- ✅ **اكتشاف تلقائي للملف الرئيسي** (`demo.ipynb`, `train.py`, `main.py`, etc.)  
  Auto-detects main script or notebook
- ✅ **تثبيت تلقائي لـ `requirements.txt`**  
  Automatically installs dependencies
- ✅ **تخزين مؤقت ذكي** لتسريع التشغيل المتكرر  
  Intelligent caching for repeated runs
- ✅ **تمرير arguments** للسكربت الأصلي  
  Full argument passing to target script
- ✅ **تنظيف كامل تلقائي** بعد الانتهاء  
  Complete automatic cleanup

---
## 🎥 ديمو سريع / Quick Demo
[![ديمو gitrun مع micrograd - افتح demo.ipynb تلقائيًا في Jupyter Lab](https://img.youtube.com/vi/aULGRDQP-iI/maxresdefault.jpg)](https://www.youtube.com/watch?v=aULGRDQP-iI)

> اضغط على الصورة لمشاهدة الديمو الكامل على YouTube (أقل من دقيقة!)
>
> شاهد كيف يقوم gitrun بتشغيل مشروع micrograd لـ Andrej Karpathy فورًا — بدون clone أو إعدادات يدوية!!

> Watch how gitrun automatically opens the `demo.ipynb` notebook from Karpathy's micrograd project in Jupyter Lab in under 10 seconds — no manual cloning or setup required!
📦📦 التثبيت / Installation
المفضل (مع عزل كامل):
Bashpipx install gitrun
ملاحظة: ننصح باستخدام pipx للتثبيت العالمي المعزول.
Recommended: Use pipx for global isolated installation.
بديل (باستخدام pip عادي):
Bashpip install gitrun
🚀 أمثلة استخدام / Usage Examples

تشغيل micrograd (المشروع الأشهر لـ Andrej Karpathy)Bashgitrun https://github.com/karpathy/micrograd→ يفتح demo.ipynb تلقائيًا في Jupyter Lab داخل المتصفح!
تشغيل nanoGPTBashgitrun https://github.com/karpathy/nanoGPT→ يشغل train.py تلقائيًا
تشغيل ملف محددBashgitrun https://github.com/user/repo --script app.py
تمرير arguments للسكربتBashgitrun https://github.com/user/repo train.py --epochs 10 --batch_size 32
وضع التفاصيل (verbose)Bashgitrun https://github.com/karpathy/llm.c -v
تشغيل بدون بيئة افتراضيةBashgitrun https://github.com/user/repo --no-venv

🤝 المساهمة / Contributing
مرحب بكل المساهمات!
Contributions are welcome!

Fork المشروع
أنشئ فرع جديدBashgit checkout -b feature/amazing
اعمل commitBashgit commit -m 'Add amazing feature'
Push الفرعBashgit push origin feature/amazing
افتح Pull Request

📄 الترخيص / License
مشروع مفتوح المصدر تحت رخصة MIT.
Open source under the MIT License - see LICENSE for details.
⭐ دعم المشروع
إذا أعجبك gitrun:

أعطِ نجمة ⭐ على GitHub
شاركه مع أصدقائك في مجتمعات البرمجة والذكاء الاصطناعي
جرب مع مشاريع Andrej Karpathy وغيرها!

شكرًا لاستخدامك gitrun!
Made with ❤️ by RACHIDHEZLA
