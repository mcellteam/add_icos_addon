
INSTALL_DIR = /Applications/Blender-2.79-CellBlender/blender.app/Contents/Resources/2.79/scripts/addons

SHELL = /bin/sh

SOURCES = ./add_icos_addon/__init__.py

ZIPFILES = $(SOURCES)

ZIPOPTS = -X -0 -D -o


all: add_icos_addon add_icos_addon.zip


add_icos_addon:
	ln -s . add_icos_addon


add_icos_addon.zip: $(SOURCES)
	@echo Updating add_icos_addon.zip
	@echo Sources = $(SOURCES)
	@zip $(ZIPOPTS) add_icos_addon.zip $(ZIPFILES)


clean:
	rm -f add_icos_addon.zip


install: add_icos_addon.zip
	@ mkdir -p $(INSTALL_DIR)
	@ unzip -o add_icos_addon.zip -d $(INSTALL_DIR); \

