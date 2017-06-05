
#include <cstdio>

int main(int argc, char *argv[])
{
	std::printf("Good Morning, My Princess!\n");

	/* 
		3d arrays operation:
		1. New
		2. delete
	*/

	int xCells = 5, yCells = 6, zCells = 7;

	// 1. new.
	double *** arr3d = new double ** [xCells];

	for ( int i=0; i<xCells; i++)
	{
		arr3d[i] = new double * [yCells];
		for (int j=0; j<yCells; j++)
			arr3d[i][j] = new double [zCells];
	}

	// 2. delete
	for ( int i=0; i<xCells; i++)
	{
		
		for (int j=0; j<yCells; j++)
			delete [] arr3d[i][j];

		delete [] arr3d[i];
	}

	delete [] arr3d;

	std::getchar();

	return true;
}