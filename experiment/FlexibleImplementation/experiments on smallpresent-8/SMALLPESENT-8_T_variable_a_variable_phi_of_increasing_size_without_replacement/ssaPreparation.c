#include<stdio.h>
#include<stdlib.h>
#include "config.h"

/* Note that this program can handle if 
   1. The no of fixed bits both in plaintext-ciphertext space have to be less or equal to 64
   2. And the number of free bits both in plaintext-ciphertext space also have to be less or equal to 64.
   If any of them is larger than 64, then those bits are always kept as zero	

   It takes the least signficant NOFIB number of bits from the integer fixation and set them as the fixation of the trail.
   Then it takes lest significant min(64,(BLOCKLENGTH*8-NOFIB)) number of bits from the integer freebits and set them as free bits of plaintext
   */

void prepareplaintext(unsigned char **plaintext_states,unsigned int **trails,unsigned long long int fixation,unsigned long long int freebits)
{
int i =0;
int j = 0;
int target_byte_position = 0;
int target_bit_position = 0;
unsigned char ith_fixed_bit_value_of_input_trail = 0x00;

	/*First initialize the plaintext_state to all zero*/

	for(i = 0; i <= ROUND; i++)
	{
		for(j = 0;j < BLOCKLENGTH; j++)
		{
			plaintext_states[i][j] = 0x00;
		}

	}

	
	for(i = 0;i < NOFIB; i++)
	{
		/* There are NOFIB number of bits in the input trail. The bits from the bitstring of the integer "fixation" will be set
		   as the fixed bits of the input of the trail. The LSB and MSB of the integer "fixation" will become the first and last bits
		   of the input trail respectively */
		ith_fixed_bit_value_of_input_trail = (fixation >> i) & 0x0000000000000001;
		/* ith fixed bit of the input trail should be fixed at some target bit position of the plaintext. 
		   This target bit position is mentioned trails[0][i]. Now the task is to find this bit position in plaintext_states[0] array  */
		target_byte_position = trails[0][i]/8;
		target_bit_position = trails[0][i]%8;

		/* Fixing the bit value to the bit position of the plaintext*/
		plaintext_states[0][target_byte_position] = plaintext_states[0][target_byte_position] ^ (ith_fixed_bit_value_of_input_trail << target_bit_position);
	}


	int no_of_free_bits = 0;
	if(BLOCKLENGTH*8-NOFIB > 64)
	{
		no_of_free_bits = 64;
	}
	else
	{
		no_of_free_bits = BLOCKLENGTH*8-NOFIB;
	}

	for(i = 0;i < no_of_free_bits; i++)
	{

		/* There are BLOCKLENGTH*8-NOFIB number of free bits in the plaintext. The bits from the 
		   bitstring of the integer "freebits" will be set as the free bits in the plaintext. 
		   The LSB and MSB of the integer "freebits" will become the first and last bits
		   of the input trail respectively */
		ith_fixed_bit_value_of_input_trail = (freebits >> i) & 0x0000000000000001;
		/* ith fixed bit of the input trail should be fixed at some target bit position of the plaintext. 
		   This target bit position is mentioned trails[0][i]. Now the task is to find this bit position in plaintext_states[0] array  */
		target_byte_position = trails[2][i]/8;
		target_bit_position = trails[2][i]%8;

		/* Fixing the bit value to the bit position of the plaintext*/
		plaintext_states[0][target_byte_position] = plaintext_states[0][target_byte_position] ^ (ith_fixed_bit_value_of_input_trail << target_bit_position);

	}
}

unsigned int** preparingtheTrail()
{

	int i;
	unsigned int x = 0;
	unsigned int **trails;

	trails = (unsigned int **)malloc(sizeof(unsigned int)*4);
	
	trails[0] = (unsigned int *)malloc(sizeof(unsigned int)*NOFIB);
	trails[1] = (unsigned int *)malloc(sizeof(unsigned int)*NOFOB);

	trails[2] = (unsigned int *)malloc(sizeof(unsigned int)*(BLOCKLENGTH*8-NOFIB)); //non trail at input
	trails[3] = (unsigned int *)malloc(sizeof(unsigned int)*(BLOCKLENGTH*8-NOFOB)); //non trail at output


	/*START: Hard coding the SSA trail inside the code. However, in below one can take it from user from standard input*/
	
	/*Trail for SMALLPRESENT-8*/
	//trail input
	trails[0][0] = 10; trails[0][1] = 11; trails[0][2] = 14; trails[0][3] = 15;
	trails[0][4] = 26; trails[0][5] = 27; trails[0][6] = 30; trails[0][7] = 31;
	
	//trail output
	trails[1][0] = 9; trails[1][1] = 11; trails[1][2] = 13; trails[1][3] = 15;
	trails[1][4] = 25; trails[1][5] = 27; trails[1][6] = 29; trails[1][7] = 31;


	/*Trail for SMALLPRESENT-4*/
	//trail input
	//trails[0][0] = 5; trails[0][1] = 6; trails[0][2] = 9; trails[0][3] = 10;
	
	
	//trail output
	//trails[1][0] = 5; trails[1][1] = 6; trails[1][2] = 9; trails[1][3] = 10;
	

	/*End: Hard coding the SSA trail inside the code. However, in below one can take it from user from standard input*/
	
	/*
	Using this commented portion of the code, someone can take the ssa trail as input from the cryptanalyst

	printf("The program is configured in config.h file. It expects %d bits input and %d bits output trail.\n",NOFIB,NOFOB);
	printf("Please Enter bit positions of the input of the trail (starting from zero at right):");
	for(i = 0; i < NOFIB; i++)
	{
		scanf("%d",&x);
		trails[0][i] = x;
	}

	printf("Enter bit positions of the output of the trail (starting from zero at right):");
	for(i = 0; i < NOFOB; i++)
	{
		scanf("%d", &x);
		trails[1][i] = x;
	} */

	int in_trail = 0;
	int j = 0;
	int k = 0;
	int l = 0;

	/*Below commplex for loop is to generate the nontrails*/
	for(i = 0; i < BLOCKLENGTH*8; i++)
	{
		/*At first check if bit position i is in the trail or not. If it is in the trail, do nothing.
		  If it is not in the trail then add it in the non-trail*/
		in_trail = 0;
		for(j = 0;j < NOFIB; j++)
		{
			if(trails[0][j] == i)
			{	
				in_trail = 1; //will indicate that bit position i is in the trail
				break;
			}
		}

		if(in_trail == 0) 
		{
			trails[2][k] = i; //bit position i is not in the input trail. taking it in input nontrails
			k++;
		}


		in_trail = 0;
		for(j = 0;j < NOFOB; j++)
		{
			if(trails[1][j] == i)
			{	
				in_trail = 1; //will indicate that bit position i is in the trail
				break;
			}
		}

		if(in_trail == 0) 
		{
			trails[3][l] = i; //bit position i is not in the trail. taking it in nontrails
			l++;
		}

	}

return trails;

}

void freeTrailMemory(unsigned int **trails)
{

free(trails[0]);
free(trails[1]);
free(trails[2]);
free(trails[3]);
free(trails);

}

void configureationConsistencyCheck()
{
char x;
int i = 0;

if(NOFIB > 64 || NOFOB > 64 || (4*n)-NOFIB > 64 || (4*n)-NOFOB > 64)
{
	printf("Note that this program can handle if \n1. The no of fixed bits both in plaintext-ciphertext space is less or equal to 64 \n2. And the number of free bits is also less or equal to 64. \nIf one of them is larger than 64, then those bits are always kept as zero. \n Do you want to continue?");
	scanf("%c",&x);

}


}


void printSSASetup(unsigned char **keys,unsigned int **trails)
{

	FILE *f;
	int i = 0;

	f = fopen("output.txt","w");
	fprintf(f,"SMALLPRESENT-[%d]\n",n);
	fprintf(f,"No of Rounds:%d\n",ROUND);
	fprintf(f,"Block size: %d bits\n",4*n);
	fclose(f);
	printMasterKey(keys);
	f = fopen("output.txt","a");
	fprintf(f,"Size of input trail:%d\n",NOFIB);
	fprintf(f,"Size of output trail:%d\n",NOFIB);
	fprintf(f,"Bit positions at the input of the trail (starting from zero from the right):");
	for(i = 0; i < NOFIB;i++)
	{
		fprintf(f,"%d ", trails[0][i]);
	}
	fprintf(f,"\n");
	/*printf("Bit positions at the input of the nontrail (starting from zero from the right):\n");
	for(i = 0; i < BLOCKLENGTH*8-NOFIB;i++)
	{
		printf("%d ", trails[2][i]);
	}
	printf("\n"); */
	fprintf(f,"Bit positions at the output of the trail (starting from zero from the right):");
	for(i = 0; i < NOFOB;i++)
	{
		fprintf(f,"%d ", trails[1][i]);
	}
	fprintf(f,"\n");
	/*printf("Bit positions at the output of nontrail (starting from zero from the right):\n");
	for(i = 0; i < BLOCKLENGTH*8-NOFOB;i++)
	{
		printf("%d ", trails[3][i]);
	}
	printf("\n"); */
	fclose(f);
}
