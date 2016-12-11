image.hex: image.script
	python script2hex.py image.script

image.script: fh1.script
	grep -v ';' fh1.script > image.script

clean:
	rm -rf `cat .gitignore`
