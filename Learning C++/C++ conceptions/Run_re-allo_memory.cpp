
#include <cstdio>
#include <cstdlib>
#include <math.h>

int main(int argc, char *argv[])
{
	std::printf("Good Morning, My Princess!\n");
	
	/*================================================================================
		Conduct test on an arbitrary direction.
	================================================================================*/
	int* numbers = NULL;
	int* more_numbers = NULL;

	numbers = (int*) std::malloc( sizeof(int) * 10 );
	more_numbers = (int*) std::realloc( numbers, sizeof(int) * 20);

	if ( more_numbers == NULL )	// re-allocating failed
	{
		std::puts( "Error (re)allocating memory!\n" );
		std::free( numbers );
	}
	else // re-allocating succeeded!
	{
		std::free(more_numbers);
		numbers[1] = 1;
		more_numbers[1] = 1;
		numbers = more_numbers;
		numbers[11] = 11;

		std::free(numbers);
	}
	
	std::getchar();
	
	return true;
}

