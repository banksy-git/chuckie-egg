INCLUDES := defs.6502 vars.6502 ChuckieOS.6502
MINIPROGS := Init.6502 KeySelect.6502 Home.6502 Game.6502 Play.6502 
BUILDDIR := ../build
MINIOBJS := $(MINIPROGS:%.6502=$(BUILDDIR)/%)
DISC := $(BUILDDIR)/Chuckie.ssd

all: $(DISC)

$(BUILDDIR)/%: %.6502 $(INCLUDES)
	beebasm -i $< -dd -labels $@.labels

$(DISC): $(MINIOBJS)
	cat $(BUILDDIR)/*.nfo > $(BUILDDIR)/addrs.inc
	beebasm -i disc.6502 \
		-do ../build/Chuckie.ssd \
		-boot CHUCKIE \
		-title Chuckie
