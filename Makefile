# Installs web2py and makes symlinks.

ROOT_DIR = $(abspath ./)
export ROOT_DIR
TARGET_WEB2PY_DIR = $(abspath web2py)
export TARGET_WEB2PY_DIR

.PHONY: all install uninstall run

all:
	$(error Please specify target. Valid targets are: install, uninstall, run)

# Run a dev server without GUI, where the admin password is '123'.
run:
	python $(TARGET_WEB2PY_DIR)/web2py.py --nogui -p 8000 -a 123

uninstall:
	rm -fr $(TARGET_WEB2PY_DIR)

install:
	$(MAKE) install -C site-packages
	@echo 'Make app symlinks...'
	ln -s $(abspath applications/web2py_translate) \
		$(abspath $(TARGET_WEB2PY_DIR)/applications/web2py_translate)
	ln -s $(abspath requirements.txt) \
		$(abspath $(TARGET_WEB2PY_DIR)/requirements.txt)
