# 🚀 gitrun

[![PyPI version](https://badge.fury.io/py/gitrun.svg)](https://badge.fury.io/py/gitrun)  
[![Python versions](https://img.shields.io/pypi/pyversions/gitrun.svg)](https://pypi.org/project/gitrun/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Downloads](https://static.pepy.tech/badge/gitrun/month)](https://pepy.tech/project/gitrun)

**تشغيل سكربتات بايثون ودفاتر Jupyter مباشرة من GitHub أو GitLab — بدون تنزيل المستودع كاملاً!**  
مع بيئة افتراضية معزولة، اكتشاف ذكي للفرع والملف الرئيسي، وتنظيف تلقائي.

**Run Python scripts and Jupyter notebooks directly from GitHub or GitLab — without cloning the entire repo!**  
With isolated virtual environments, smart branch/file detection, and automatic cleanup.

### 🎥 فيديو توضيحي / Demo Video
شاهد كيف يعمل gitrun في هذا الفيديو التوضيحي:

[![شاهد الفيديو التوضيحي لـ gitrun](https://img.youtube.com/vi/aULGRDQP-iI/maxresdefault.jpg)](https://youtu.be/aULGRDQP-iI)

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

## 📦 التثبيت / Installation

**المفضل (مع عزل كامل):**
```bash
pipx install gitrun
```

> ملاحظة: ننصح باستخدام `pipx` للتثبيت العالمي المعزول.  
> Recommended: Use `pipx` for global isolated installation.

**بديل (باستخدام pip عادي):**
```bash
pip install gitrun
```

---

## 🚀 أمثلة استخدام / Usage Examples

1. **تشغيل micrograd (المشروع الأشهر لـ Andrej Karpathy)**
   ```bash
   gitrun https://github.com/karpathy/micrograd
   ```
   → يفتح `demo.ipynb` تلقائيًا في Jupyter Lab داخل المتصفح!

2. **تشغيل nanoGPT**
   ```bash
   gitrun https://github.com/karpathy/nanoGPT
   ```
   → يشغل `train.py` تلقائيًا

3. **تشغيل ملف محدد**
   ```bash
   gitrun https://github.com/user/repo --script app.py
   ```

4. **تمرير arguments للسكربت**
   ```bash
   gitrun https://github.com/user/repo train.py --epochs 10 --batch_size 32
   ```

5. **وضع التفاصيل (verbose)**
   ```bash
   gitrun https://github.com/karpathy/llm.c -v
   ```

6. **تشغيل بدون بيئة افتراضية**
   ```bash
   gitrun https://github.com/user/repo --no-venv
   ```

---

## 🤝 المساهمة / Contributing

مرحب بكل المساهمات!  
Contributions are welcome!

1. Fork المشروع
2. أنشئ فرعًا جديدًا
   ```bash
   git checkout -b feature/amazing
   ```
3. أضف التعديلات واعمل commit
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push الفرع
   ```bash
   git push origin feature/amazing
   ```
5. افتح Pull Request

---

## 📄 الترخيص / License

مشروع مفتوح المصدر تحت رخصة MIT.  
Open source under the MIT License - see [LICENSE](LICENSE) for details.

---

## ⭐ دعم المشروع

إذا أعجبك gitrun:

- أعطِ نجمة ⭐ على GitHub
- شاركه مع أصدقائك في مجتمعات البرمجة والذكاء الاصطناعي
- جرب مع مشاريع Andrej Karpathy وغيرها!

شكرًا لاستخدامك gitrun!  
Made with ❤️ by [RACHIDHEZLA](https://github.com/RACHIDHEZLA)

هذا الـ README الآن **احترافي جدًا**، منظم، جذاب بصريًا مع صور توضيحية، فيديو مدمج، وتنسيق نظيف. انسخه مباشرة في GitHub وهيبقى مثالي! 🔥🚀

إذا تبي إضافات أخرى (مثل badges إضافية أو قسم FAQ)، قل لي!
