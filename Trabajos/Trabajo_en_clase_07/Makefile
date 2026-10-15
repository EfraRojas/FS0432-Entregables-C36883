TARGET = gauss

CXX = g++
# Se añade -undefined dynamic_lookup para macOS
CXXFLAGS = -O3 -std=c++17 -shared -fPIC -undefined dynamic_lookup

PYTHON_INCLUDE = $(shell python3 -m pybind11 --includes)
PYTHON_SUFFIX = $(shell python3-config --extension-suffix)

SRC = gauss.cpp
OUTPUT = $(TARGET)$(PYTHON_SUFFIX)

all: $(OUTPUT)

$(OUTPUT): $(SRC)
	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDE) $(SRC) -o $(OUTPUT)

clean:
	rm -f $(OUTPUT)
