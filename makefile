all: quicksort

quicksort: quicksort.o
	g++ quicksort.o -o quicksort

quicksort.o: quicksort.cpp
	g++ -c quicksort.cpp

clean:
	rm -rf *.o quicksort