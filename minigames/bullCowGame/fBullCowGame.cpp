#include "fBullCowGame.h"

void fBullCowGame::reset(){

}

int fBullCowGame::getMaxTries(){
	return myMaxTries;
}

int fBullCowGame::getCurrentTry(){
	return myCurrentTry;
}

bool fBullCowGame::isGameWon(){
	return false;
}

bool fBullCowGame::checkGuesValid(std::string){
	return false;
}
