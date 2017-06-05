

// rvalue-references-move-semantics.cpp
// compile with: /EHsc
#include "MemoryBlock.h"
#include <vector>


int main()
{
	std::printf("Good Morning, My Princess!\n");
	// Create a vector object and add a few elements to it.
	std::vector<MemoryBlock> v;

	MemoryBlock A(35);
	
	v.push_back(MemoryBlock(35));	// invoke move operation, because the object is tempery.
	v.push_back(A);					// invoke copy operation, due to the existence of A.
	v.push_back(std::move(A));		// Force invoke Move operation
		

	// Insert a new element into the second position of the vector.
	v.insert(v.begin() + 1, MemoryBlock(50));

	std::getchar();

	return true;
}
