PYTHON_VERSION=
PYTHON_ENV_TEST=env-test$(PYTHON_VERSION)
all: clean env tests

env: env/bin/activate

env/bin/activate:
	bin/env.sh

test:
	bin/tests.sh $(PYTHON_VERSION)

test-clean:
	rm -Rf env-tes*

clean:
	bin/clean.sh

