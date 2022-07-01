import inspect
import logging
from contextlib import contextmanager

try:
    import sentry_sdk
except ImportError:
    pass


@contextmanager
def logger_handler(command):
    try:
        yield
    except (KeyboardInterrupt, SystemExit):
        pass
    except Exception as exc:
        module = inspect.getmodule(command)
        logger = logging.getLogger(module.__name__)
        logger.exception(f'Error while running command: {command.command_name}')
        raise exc from None


@contextmanager
def sentry_handler(command):
    def processor(event, hint):
        event['transaction'] = command.command_name

    assert sentry_sdk
    hub = sentry_sdk.Hub.current
    with sentry_sdk.Hub(hub) as hub:
        with hub.configure_scope() as sentry_scope:
            sentry_scope.add_event_processor(processor)
            try:
                yield
            except (KeyboardInterrupt, SystemExit):
                pass
            except Exception as exc:
                hub.capture_exception(exc)
                raise exc from None
