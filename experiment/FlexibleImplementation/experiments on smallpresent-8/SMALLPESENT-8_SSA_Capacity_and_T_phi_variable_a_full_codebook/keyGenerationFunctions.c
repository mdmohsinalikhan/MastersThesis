#include<stdio.h>
#include<stdlib.h>
#include "config.h"

/* This file contains all the functions required for generating the keys*/


//the following function considers the key in keys[0][i] to be the master key
unsigned char**  generateRoundKeys()
{

	int i = 1;
	unsigned char **keys = (unsigned char **)malloc(sizeof(unsigned char*)*(ROUND+1));

	for(i = 0;i <= ROUND; i++)
	{
		keys[i] = (unsigned char *)malloc(sizeof(unsigned char)*KEYLENGTH*8);
	}	


	//initialize the master key
	keys[0][0] = KEYS00; keys[0][1] = KEYS01; keys[0][2] = KEYS02; keys[0][3] = KEYS03; keys[0][4] = KEYS04;
	keys[0][5] = KEYS05; keys[0][6] = KEYS06; keys[0][7] = KEYS07; keys[0][8] = KEYS08; keys[0][9] = KEYS09;

	int j = 1;
	for(i = 1; i <= ROUND; i++)
	{
		rotateKey61bitLeft(i, keys);
		applySBoxOnKey(i, keys);
		addRoundCounterOnKey(i, keys);
	}

	//just to test if the round keys are correct
	//printRoundKeys(keys);

return keys;
}


void rotateKey61bitLeft(int r,unsigned char **keys)
{
	keys[r][0]=keys[r-1][2] >> 3;
	keys[r][0]= keys[r][0] ^ (keys[r-1][3] & 0x07) << 5;

	keys[r][1]=keys[r-1][3] >> 3;
	keys[r][1]= keys[r][1] ^ (keys[r-1][4] & 0x07) << 5;

	keys[r][2]=keys[r-1][4] >> 3;
	keys[r][2]= keys[r][2] ^ (keys[r-1][5] & 0x07) << 5;

	keys[r][3]=keys[r-1][5] >> 3;
	keys[r][3]= keys[r][3] ^ (keys[r-1][6] & 0x07) << 5;

	keys[r][4]=keys[r-1][6] >> 3;
	keys[r][4]= keys[r][4] ^ (keys[r-1][7] & 0x07) << 5;

	keys[r][5]=keys[r-1][7] >> 3;
	keys[r][5]= keys[r][5] ^ (keys[r-1][8] & 0x07) << 5;

	keys[r][6]=keys[r-1][8] >> 3;
;	keys[r][6]= keys[r][6] ^ (keys[r-1][9] & 0x07) << 5;


	keys[r][7]=keys[r-1][9] >> 3;
	keys[r][7]= keys[r][7] ^ (keys[r-1][0] & 0x07) << 5;

	keys[r][8]=keys[r-1][0] >> 3;
	keys[r][8]= keys[r][8] ^ (keys[r-1][1] & 0x07) << 5;

	keys[r][9]=keys[r-1][1] >> 3;
	keys[r][9]= keys[r][9] ^ (keys[r-1][2] & 0x07) << 5;
}


void applySBoxOnKey(int r,unsigned char **keys)
{
	unsigned char input;
	input = keys[r][9] >> 4;
	keys[r][9] = (keys[r][9] & 0x0f) ^ (sBox(input) << 4);	
}


void addRoundCounterOnKey(int r,unsigned char **keys)
{
	keys[r][2] = keys[r][2] ^ (r >> 1);
	keys[r][1] = keys[r][1] ^ (r << 7);
}


void printRoundKeys(unsigned char **keys)
{
	int i = 0;
	int j = 0;
	for(i = 0; i <= ROUND; i++)
	{
		printf("Round key at %d round: ",i);
		for(j = 0; j < 10; j++)
		{
			printf("%02X ",keys[i][j]);
		}
		printf("\n");		
	}

}

void printMasterKey(unsigned char **keys)
{

	FILE *f;
	f = fopen("output.txt","a");
	int i = 0;
	int j = 0;
	for(i = 0; i < 1; i++)
	{
		fprintf(f,"Master Key:");
		for(j = 0; j < 10; j++)
		{
			fprintf(f,"%02X ",keys[0][j]);
		}
		fprintf(f,"\n");		
	}
	fclose(f);

}

//To release keys, plaintext states and ciphertext states
void releaseKeyMemory(unsigned char **states)
{
	int i = 0;
	for(i = 0;i <= ROUND; i++)
	{
		free(states[i]);
	}	

	free(states);
}
