import os
import fcntl
import pyinotify
import logging
import config
import Watcher.EventHandler


def main():

    # acquire the prog lock
    if not prog_lock_acq('singleton.lock'):
        print("another instance is running")
        exit(1)

    print("program is running-press Ctrl+C to stop")
    
    #
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY | pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO

    # add the path we want to watch
    wm.add_watch(config.Watcher.path, mask, rec = config.Watcher.recursively, auto_add = config.Watcher.auto_add)


    # configure the logguer
    logging.basicConfig(filename = config.Watcher.log_filename, level = logging.DEBUG)

    #
    notifier = pyinotify.Notifier(wm, Watcher.EventHandler.Handler(logging))
    notifier.loop()


def prog_lock_acq(path):
    fd = None
    try:
        fd = os.open(path, os.O_CREAT)
        fcntl.flock(fd, fcntl.LOCK_NB | fcntl.LOCK_EX)
        return True
    except (OSError, IOError):
        if fd:
            os.close(fd)

        return False

if __name__ == '__main__':
    main()
