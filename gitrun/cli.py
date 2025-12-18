#!/usr/bin/env python3
"""
واجهة سطر الأوامر لـ gitrun
"""
import sys
import argparse
from gitrun.core import GitRunner

def main():
    # طباعة للتحقق
    print("🔍 sys.argv:", sys.argv, file=sys.stderr)
    
    parser = argparse.ArgumentParser(
        description='gitrun - تشغيل سكربتات بايثون مباشرة من GitHub/GitLab',
        add_help=False
    )
    
    # ال arguments الخاصة بنا
    parser.add_argument('repo', help='رابط المستودع')
    parser.add_argument('-s', '--script', help='اسم السكربت المراد تشغيله')
    parser.add_argument('-b', '--branch', default='main', help='فرع المستودع')
    parser.add_argument('-v', '--verbose', action='store_true', help='عرض معلومات تفصيلية')
    parser.add_argument('--no-venv', action='store_true', help='تشغيل بدون بيئة افتراضية')
    parser.add_argument('--help', action='help', help='عرض رسالة المساعدة هذه')
    parser.add_argument('--version', action='version', version='gitrun 0.1.0')
    
    # باقي ال arguments (سيكون للسكربت الأصلي)
    parser.add_argument('extra_args', nargs='*', help='Arguments للسكربت الأصلي')
    
    # Parse ال arguments
    args, unknown = parser.parse_known_args()
    
    print("🔍 args بعد parsing:", args, file=sys.stderr)
    print("🔍 unknown args:", unknown, file=sys.stderr)
    
    # إنشاء وتشغيل GitRunner
    runner = GitRunner(
        repo_url=args.repo,
        branch=args.branch,
        script=args.script,
        verbose=args.verbose,
        use_venv=not args.no_venv
    )
    
    runner.run(args.extra_args)

if __name__ == '__main__':
    main()
