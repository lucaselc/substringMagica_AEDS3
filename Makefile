tp3:
	$(MAKE) -C src
	cp src/tp3 tp3

clean:
	$(MAKE) -C src clean
	rm -f tp3

.PHONY: clean tp3
