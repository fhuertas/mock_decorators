PYTHON_VERSION=
PYTHON_ENV_TEST=env-test$(PYTHON_VERSION)
all: clean env tests

env:
	bin/env.sh

test: $(PYTHON_ENV_TEST)
	bin/tests.sh $(PYTHON_VERSION)

test-clean:
	rm -Rf env-test*

clean:
	bin/clean.sh

$(PYTHON_ENV_TEST):
