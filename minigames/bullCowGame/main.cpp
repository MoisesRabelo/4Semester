#include <iostream>
#include <string>
#include "fBullCowGame.h"


//functions
void intro();
void playGame();
std::string getGuess();
bool askToPlayAgain();

fBullCowGame BCGame;

int main() {	

	do {
		intro();
		playGame();

	} while (askToPlayAgain());

	system("pause");

	return 0;
}

void intro(){

	constexpr int word_lenght = 5;

	//intro the game
	std::cout << "Welcome to Bulls and Cows, a fun word game.\n";
	std::cout << "Can you guess the " << word_lenght;
	std::cout << " isogram i'm thinking of?\n";
	std::cout << std::endl;

	return;
}

std::string getGuess() {

	
	int static currentTry = BCGame.getCurrentTry();

	std::cout << "\tTry : " << currentTry << std::endl;

	//get the guess from the player
	std::cout << "Enter your guess!\n";

	std::string guess = "";

	

	std::getline(std::cin, guess);
	currentTry++;
	return guess;
}

void playGame() {

	int maxTries = BCGame.getMaxTries();
	std::cout << maxTries << std::endl;

	//loop for the number of turns
	constexpr int number_of_turns = 5;
	for (int count = 0; count < number_of_turns; count++) {
		//scan the guess and print
		std::string guess = getGuess();

		//print the guessed
		std::cout << "Your guess was : ";
		std::cout << guess << std::endl << std::endl;

	}

	return;
}


bool askToPlayAgain() {
	
	std::string choice;

	std::cout << "Do you want to play again? (y/n)\n";
	std::getline(std::cin,choice);

	return (choice[0] == 'y') || (choice[0] == 'Y');
}
