all:
	@mkdir -p build
	$(MAKE) -C src

clean:
	@rm -rf build
