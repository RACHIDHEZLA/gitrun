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

<video controls width="100%">
  <source src="demo.mp4" type="video/mp4">
  متصفحك لا يدعم تشغيل الفيديو / Your browser does not support the video tag.
</video>

> شاهد كيف يقوم gitrun بفتح دفتر `demo.ipynb` من مشروع micrograd تلقائيًا في Jupyter Lab في أقل من 10 ثواني — بدون أي تنزيل يدوي أو إعدادات!

> Watch how gitrun automatically opens the `demo.ipynb` notebook from Karpathy's micrograd project in Jupyter Lab in under 10 seconds — no manual cloning or setup required!


## 📦 التثبيت / Installation

```bash
pipx install gitrun
ملاحظة: ننصح باستخدام pipx للعزل الكامل
Recommended: Use pipx for global isolated installation
أو بـ pip عادي:
Bashpip install gitrun

🚀 أمثلة استخدام / Usage Examples
1. تشغيل micrograd (المشروع الأشهر لـ Andrej Karpathy)
Bashgitrun https://github.com/karpathy/micrograd
→ يفتح demo.ipynb تلقائيًا في Jupyter Lab داخل المتصفح!
2. تشغيل nanoGPT
Bashgitrun https://github.com/karpathy/nanoGPT
→ يشغل train.py تلقائيًا
3. تشغيل ملف محدد
Bashgitrun https://github.com/user/repo --script app.py
4. تمرير arguments للسكربت
Bashgitrun https://github.com/user/repo train.py --epochs 10 --batch_size 32
5. وضع التفاصيل (verbose)
Bashgitrun https://github.com/karpathy/llm.c -v
6. تشغيل بدون بيئة افتراضية
Bashgitrun https://github.com/user/repo --no-venv



🤝 المساهمة / Contributing
مرحب بكل المساهمات!
Contributions are welcome!

Fork المشروع
أنشئ فرع جديد (git checkout -b feature/amazing)
اعمل commit (git commit -m 'Add amazing feature')
Push الفرع (git push origin feature/amazing)
افتح Pull Request


📄 الترخيص / License
مشروع مفتوح المصدر تحت رخصة MIT
Open source under the MIT License - see LICENSE for details.

⭐ دعم المشروع
إذا أعجبك gitrun:

أعطِ نجمة ⭐ على GitHub
شاركه مع أصدقائك في مجتمعات البرمجة والذكاء الاصطناعي
جرب مع مشاريع Andrej Karpathy وغيرها!

شكرًا لاستخدامك gitrun!
Made with ❤️ by RACHIDHEZLA
```
