#pragma once
#include<string>

class fBullCowGame{
public:
	void reset();
	int getMaxTries();
	int getCurrentTry();
	bool isGameWon();
	bool checkGuesValid(std::string);

	    

private:

	int myCurrentTry = 1;
	int myMaxTries = 5;


};
