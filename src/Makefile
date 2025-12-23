INCLUDES := defs.6502 vars.6502 ChuckieOS.6502
MINIPROGS := Init.6502 KeySelect.6502 Home.6502 Game.6502 Play.6502 Loader.6502
BUILDDIR := ../build
MINIOBJS := $(MINIPROGS:%.6502=$(BUILDDIR)/%)
DISC := $(BUILDDIR)/Chuckie.ssd

all: $(DISC)

git_version:
	@TAG=$$(git describe --tags --always --dirty); \
	echo "    EQUS \"$$TAG\", 0" > $(BUILDDIR)/version.inc

$(BUILDDIR)/%: %.6502 $(INCLUDES) git_version
	beebasm -i $< -dd -labels $@.labels

$(DISC): $(MINIOBJS) disc.6502
	cat $(BUILDDIR)/*.nfo > $(BUILDDIR)/addrs.inc
	beebasm -i disc.6502 \
		-do ../build/Chuckie.ssd \
		-boot LOADER \
		-title Chuckie
