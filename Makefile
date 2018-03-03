LOCAL_SITE_PACKAGES=$(shell python3 -m site --user-site)

install:
	cp -a libs/* $(LOCAL_SITE_PACKAGES)

clean:
	@rm -rf build/ dist/ *.egg-info
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*.un~' -exec rm -f {} +

