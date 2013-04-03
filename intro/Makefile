index.tgz: index.html
	tar czf $@ $< theme/

index.html: index.md
	landslide -r -c $< -d $@

clean:
	rm -f index.html index.tgz
	rm -rf theme/
