from django.core.checks import Warning, register
from django.core.checks import Tags as DjangoTags
from django.conf import settings

from flake8.main import application as app
import flake8


class Tags(DjangoTags):
    lints = 'lints'


@register(Tags.lints)
def lint2(app_configs, **kwargs):
    application = app.Application()

    application.parse_preliminary_options_and_args([])
    application.make_config_finder()

    application.find_plugins()
    application.register_plugin_options()

    application.parse_configuration_and_cli([])

    options = application.options
    if hasattr(settings, 'LINT2'):
        for key, value in settings.LINT2.items():
            setattr(options, key, value)

    setattr(options, 'exclude', ['*migrations*', 'manage.py', '.git', 'settings.py'])

    application.make_formatter(flake8.formatting.default.Nothing)
    application.make_notifier()
    application.make_guide()
    application.make_file_checker_manager()

    application.run_checks()
    application.report_errors()

    errors = []
    for checker in application.file_checker_manager.checkers:
        for err in checker.results:
            errors.append(Warning(
                f'{checker.filename}:{err[1]}:{err[2]}:{err[3]}',
                id=err[0],
            ))
    return errors
