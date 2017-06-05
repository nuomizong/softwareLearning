#include <cstdio>
#include <cstdlib>

#include <vector>
#include <map>

int main(int argc, char ** argv)
{
	std::printf("Good Morning, My Princess!\n");

	std::vector< std::map<int, float> > book;

	std::map<int, float> emptyMap;
	book.push_back(emptyMap);

	std::pair<int, float> entry;

	entry.first = 3;
	entry.second = 0.3f;

	book[0].insert(entry);

	entry.first = 2;
	entry.second = 0.2f;

	book[0].insert(entry);

	entry.first = 1;
	entry.second = 0.1f;

	book[0].insert(entry);

	book[0].erase(1);

	
	int count =book[0].size();

	/*for(int i=0; i<book[0].size(); i++)
	{
		std::map<int, float>::const_iterator pos = book[0].find(3);
		std::printf("entry[%d] = <%d, %f>\n", i, pos->first, pos->second);
	}*/

	for(std::map<int, float>::const_iterator pos = book[0].begin(); pos != book[0].end(); pos++)
	{
		std::printf("book[0].entry = <%d, %f>\n", pos->first, pos->second);
	}

	std::vector<int> myvector;

	// set some values (from 1 to 10)
	for (int i=1; i<=10; i++) myvector.push_back(i);

	// erase the 6th element
	myvector.erase (myvector.begin()+5);

	// erase the first 3 elements:
	myvector.erase (myvector.begin(),myvector.begin()+3);

	std::printf( "myvector contains:");
	for (unsigned i=0; i<myvector.size(); ++i)
		std::printf(" %d", myvector[i]);
	std::printf("\n");

	std::getchar();
	EXIT_SUCCESS;
}