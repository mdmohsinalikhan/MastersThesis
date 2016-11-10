#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "config.h"

void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{
	unsigned long long int **fixations_vs_output_count;
	fixations_vs_output_count = countFixationVsOutput(plaintext_states,keys,trails);

	//releasecountFixationVsOutputMemory(fixations_vs_output_count);
}

unsigned long long int ** countFixationVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{

	int i = 0;
	int j = 0;
	int total_fixations = pow(2,NOFIB);
	int total_outputs = pow(2,NOFOB);
	unsigned long long int fixation=0;
	unsigned long long int freebits=0;
	unsigned long long int total_freebit_plaintexts = pow(2,(BLOCKLENGTH*8-NOFIB));
	unsigned long long int **fixations_vs_output_count = (unsigned long long int**)malloc(sizeof(unsigned long long int*)*total_fixations);

	for(i=0; i < total_fixations; i++)
	{
	fixations_vs_output_count[i] = (unsigned long long int *)malloc(sizeof(unsigned long long int)*total_outputs);			
	}

	/*Note that we have create a two dimensional array. 
	 > fixations_vs_output_count[i] represents fixations.
	 > fixations_vs_output_count[i][j] represents fixation i and outputj. Fixation is represented by "a" in theory
		
	 In other words, the above array stores $p_{\eta}(a)$ */

	/*The container for counting is ready. Now, Let us encrypt all the possible plaintexts 
	  for all the possible fixations, for all the possible rounds and populate the array that we just have constructed above*/

	total_fixations = 2;
	total_freebit_plaintexts = 4;
	for(fixation = 0;fixation < total_fixations;fixation++)
	{
		for(freebits =0;freebits < total_freebit_plaintexts; freebits++)
		{
			prepareplaintext(plaintext_states,trails,fixation,freebits);	
			encryption(plaintext_states,keys);	
		}

	}

	return fixations_vs_output_count;
}

void releasecountFixationVsOutputMemory(unsigned long long int **fixations_vs_output_count)
{
	int i = 0;
	int j = 0;
	int total_fixations = pow(2,NOFIB);

	for(i=0; i < total_fixations; i++)
	{
		free(fixations_vs_output_count[i]);
	}
		
	free(fixations_vs_output_count);
}
