#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<string.h>
#include "config.h"


/*To compute SSA capacity of every round, we run this program for 31 rounds. After every round during an encryption, we do some bookkeeping
  To do the bookkeeping after every round, we are in need of some modification in the encryption function. We have send the pointer of array fixations_vs_output_count to the encryption function. As a result its prototype and definition is changed from the original implementation*/

void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails)
{
	unsigned long long int i = 0;
	unsigned long long int samplesize = pow(2,4*n-NOFIB);
	unsigned long long int* sample_plaintext_set = generateSampleWithoutreplacement();

	/*start: temporary code*/
		//for(i=0; i < samplesize; i++)
		//{
		//	printf("%llu ",sample_plaintext_set[i]);
		//}
	/*start: temporary code*/


	/* For all possible fixations, it will encrypt all possible plaintexts and store the observed number of a specific output
	   for a given round, fixation and size of the sample in an array and returns the pointer to the array*/
	unsigned long long int ****fixations_vs_output_count;
	fixations_vs_output_count = countFixationVsOutput(plaintext_states,keys,trails,sample_plaintext_set);

	//checking the container
	//printFixationsVsOutputCount(fixations_vs_output_count);

	/* Compute the mean and variance of $p_{\eta}(a)$ over all possible fixation for a given round
	   The result is stored in an array and the pointer to the array is returned */
	////long double ***mean_variance_p_eta;
	////mean_variance_p_eta = computeMeanVariancePEta(fixations_vs_output_count);

	/* Compute the variance of "variance of $p_{\eta}(a)$ over all possible fixation for a given round"
		over all possible $\eta$. The result is stored in an array and the pointer to the array is returned */
	////long double *variance_variance_p_eta;
	////variance_variance_p_eta = computeVarianceVariancePEta(mean_variance_p_eta);

		
	/* Computing the experimental SSA capacities i.e. $C(a)$ for a given round and fixation $a$.
	   the result is stored in an array and the pointer of the array is returned*/
	////long double ***ssa_capacities;
	////ssa_capacities = prepareSSACapacities(fixations_vs_output_count);
	
	/* 1. Compute mean and variance of experimental SSA capacities over all the fixations for every round. 
	   2. Then compute the theoretical variance of the SSA capacities over all the fixations for every round
	   3. And also compute the distance between the theoretical and experimental values of the variances of 
		SSA capacities over all fixations for every round
	   The results are stored in an array and the pointer to that array is returned*/
	////long double **ssa_capacities_mean_variance_table;
	////ssa_capacities_mean_variance_table = computeSSACapacityTable(ssa_capacities);

	/*
	   The below function prints the result we are expecting from this SSA experiment
	   1. It prints the average SSA capacity of every round
	   2. It prints the experimental variance of SSA capacities over all possible fixations a for every round
	   3. It prints the theoretical variance of SSA capacities over all possible fixations a for every round
	   4. It prints the distance between theoretical and experimental variance
	   5. It also prints the variance of "variance of $p_{\eta}(a)$ over all possible fixation for a given round"
		over all possible $\eta$
	   */
	////printf("\n\nBelow, we print the result we are expecting from this SSA experiment \n 1. It prints the average SSA capacity of every round\n 2. It prints the experimental variance of SSA capacities over all possible fixations a for every round \n 3. It prints the theoretical variance of SSA capacities over all possible fixations a for every round. \n 4. It prints the distance between theoretical and experimental variance. \n 5. It also prints the variance of 'variance of $p_{eta}(a)$ over all possible fixation for a given round' over all possible $eta$");
	///printSSACapacityDetailTable(ssa_capacities_mean_variance_table,variance_variance_p_eta);


	/* Now, we will be computing the experimental $T(\phi,a)$ for a given round,fixation and samplesize $a$*/
	long double ***T_variable_phi_variable_a;
	T_variable_phi_variable_a = prepareTphia(fixations_vs_output_count);

	//checking the values of T_variable_phi_variable_a
	//printT_variable_phi_variable_a(T_variable_phi_variable_a);

	preparePythonScriptForPlotting(T_variable_phi_variable_a);


	/* Now we will be computing the mean and varaince of $T(\phi,a)$ over all fixations and samples. 
	   As we have used the whole codebook, there will be no variance of this statistic because of $\phi$. 
	   We will compute the experimental variance over all possible a. We will also compute the theoretical 
	   variance. While computing the theoretical variance, we will have to use the formuala developed
	   for sampling without replacement. We have not developed the formula in detail in the thesis. But it 
	   is clear that the theoretical mean will be $NC$ and theoretical variance will be $\frac{2(NC)^2}{2^q-1}$. 
	   Where $N$ is the size of sample and $C$ is the average SSA capacity for that round. 
	   The result is stored in an array and the pointer of the array is returned.
	*/

	////printf("\n\n Now we will be computing the mean and varaince of $T(phi,a)$ over all fixations and samples.  \nAs we have used the whole codebook, there will be no variance of this statistic because of $phi$. \n We will compute the experimental variance over all possible a. We will also compute the theoretical variance. \n While computing the theoretical variance, we will have to use the formuala developed for sampling without replacement. \nWe have not developed the formula in detail in the thesis. But it is clear that the theoretical mean will be $NC$ and theoretical variance will be $frac{2(NC)^2}{2^q-1}$. \n Where $N$ is the size of sample and $C$ is the average SSA capacity for that round. The result is stored in an array and the pointer of the array is returned.");
	////long double **T_phi_a_mean_variance_table;
	////T_phi_a_mean_variance_table = prepareTphiaTable(T_variable_phi_variable_a,ssa_capacities_mean_variance_table);
	////print_T_phi_a_DetailTable(T_phi_a_mean_variance_table,variance_variance_p_eta);
	
	/*Releasing allocated memory*/
	////releaseSSACapacitiesMemory(ssa_capacities);
	releasecountFixationVsOutputMemory(fixations_vs_output_count);
	////releasecomputeMeanVariancePEtaMemory(mean_variance_p_eta);
	////releasecomputeSSACapacityTableMemory(ssa_capacities_mean_variance_table);
	////releasecomputeVarianceVariancePEtaMemory(variance_variance_p_eta);
	releaseprepareTphiaMemory(T_variable_phi_variable_a);
	////releaseprepareTphiaTableMemory(T_phi_a_mean_variance_table);
	free(sample_plaintext_set);
}

unsigned long long int ****countFixationVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails,unsigned long long int *sample_plaintext_set)
{

	int i = 0;
	unsigned long long int j = 0;
	unsigned long long int k = 0;
	unsigned long long int total_fixations = pow(2,NOFIB);
	unsigned long long int total_outputs = pow(2,NOFOB);
	unsigned long long int fixation=0;
	unsigned long long int freebits=0;
	unsigned long long int total_freebit_plaintexts = pow(2,(BLOCKLENGTH*8-NOFIB));
	unsigned long long int	****fixations_vs_output_count = (unsigned long long int****)malloc(sizeof(unsigned long long int***)*(ROUND+1));

	for(i = 0;i <= ROUND; i++)
	{
		fixations_vs_output_count[i] = (unsigned long long int***)malloc(sizeof(unsigned long long int**)*((4*n-NOFIB)+1));
		for(j = 0;j <= (4*n-NOFIB);j++)
		{
			fixations_vs_output_count[i][j] = (unsigned long long int**)malloc(sizeof(unsigned long long int*)*total_fixations);
			for(k=0; k < total_fixations; k++)
			{
				fixations_vs_output_count[i][j][k] = (unsigned long long int *)malloc(sizeof(unsigned long long int)*total_outputs);			
			}
		}
	}

	initialize_fixations_vs_output_count(fixations_vs_output_count);

	/*Note that we have create a two dimensional array. 
	 > fixations_vs_output_count[i] represents fixations.
	 > fixations_vs_output_count[i][j] represents fixation i and outputj. Fixation is represented by "a" in theory
		
	 In other words, the above array stores $p_{\eta}(a)$ */

	/*The container for counting is ready. Now, Let us encrypt all the possible plaintexts 
	  for all the possible fixations, for all the possible rounds and populate the array that we just have constructed above*/

	//total_fixations = 1;
	//total_freebit_plaintexts = 1;
	unsigned long long int x = 2;

	printf("Encryption is starting at: "); print_time();

	int phi_size = 0;
	
		for(fixation = 0;fixation < total_fixations;fixation++)
		{
			x = 2;
			for(freebits = 0;freebits < total_freebit_plaintexts; freebits++)
			{

				/*if((freebits+1) % x == 0)
				{
					printf("Fixation: %llu, Number of encryption Completed:%llu at ",fixation,x); print_time();
					x = x*2;
				}*/
				prepareplaintext(plaintext_states,trails,fixation,sample_plaintext_set[freebits]);	
				phi_size = computePhiSize(freebits);
				encryption(plaintext_states,keys,fixation,fixations_vs_output_count,trails,phi_size);	
			}

			printf("All encryptions for fixation %llu has been completed at: ",fixation); print_time();

		}
	return fixations_vs_output_count;
}

unsigned int computePhiSize(unsigned long long int freebits)
{

	int count = 0;
	while(freebits != 0)
	{
		freebits = freebits >> 1;
		count++;
	}

	return count;
}

void releasecountFixationVsOutputMemory(unsigned long long int ****fixations_vs_output_count)
{
	unsigned long long int i = 0;
	unsigned long long int j = 0;
	unsigned long long int k = 0;
	unsigned long long int total_fixations = pow(2,NOFIB);

	for(i = 0; i<=ROUND; i++)
	{	
		for(j=0; j <= (4*n-NOFIB); j++)
		{
			for(k=0;k < total_fixations; k++)
			{
				free(fixations_vs_output_count[i][j][k]);
			}
			free(fixations_vs_output_count[i][j]);
		}
		free(fixations_vs_output_count[i]);
	}	
	free(fixations_vs_output_count);
}

void postRoundSSABookKeping(int round,unsigned char **plaintext_states,unsigned long long int fixation,unsigned long long int ****fixations_vs_output_count,unsigned int **trails,unsigned int phi_size)
{
	unsigned int i = 0;
	unsigned long long int value_at_output_of_trail = 0;
	value_at_output_of_trail = evaluateOutputOfTrail(round,plaintext_states,trails);//checking the value of eta;
	for(i = phi_size;i <= (4*n-NOFIB); i++)
	{
		fixations_vs_output_count[round][i][fixation][value_at_output_of_trail] = fixations_vs_output_count[round][i][fixation][value_at_output_of_trail] + 1;
	}
}

unsigned long long int evaluateOutputOfTrail(int round,unsigned char **plaintext_states,unsigned int **trails)
{
int j = 0;
unsigned long long int value_at_output_of_trail=0;
unsigned int target_output_byte = 0;
unsigned int target_output_bit = 0;
unsigned long long int bit_value_at_outputput_bit_position = 0x00;
unsigned long long int x = 0;

	for(j = 0;j < NOFOB; j++)
	{
		target_output_byte = trails[1][j]/8;
		target_output_bit = trails[1][j]%8;
		x = 1 << target_output_bit;
		bit_value_at_outputput_bit_position = (plaintext_states[round][target_output_byte] & x) >> target_output_bit;
		value_at_output_of_trail = value_at_output_of_trail ^ (bit_value_at_outputput_bit_position << j);
	}
	
	/* for dummy purpose it is always returning 0 now. Soon this function will be properly implemented */
	return value_at_output_of_trail; 
}


void initialize_fixations_vs_output_count(unsigned long long int ****fixations_vs_output_count)
{
unsigned long long int i=0;
unsigned long long int j=0;
unsigned long long int k=0;
unsigned long long int l=0;

unsigned long long int total_fixations = pow(2,NOFIB);
unsigned long long int total_outputs = pow(2,NOFOB);

	for(i = 0;i <=ROUND; i++)
	{
		for(j=0; j <= (4*n - NOFIB); j++)
		{
			for(k=0; k < total_fixations; k++ )
			{
				for(l = 0; l < total_outputs; l++)
				{
					fixations_vs_output_count[i][j][k][l] = 0;
				}
			}
		}
	}	
}


void printT_variable_phi_variable_a(long double ***T_variable_phi_variable_a)
{

int i =0;
int j = 0;
unsigned long long int k = 0;
unsigned long long int total_fixations = pow(2,NOFIB);

	for(i = 0; i<= ROUND; i++)
	{
		for(j = 0; j <= (int)(4*n-NOFIB); j++)
		{
			for(k = 0; k < total_fixations;k++)
			{
				printf("T_variable_phi_variable_a[%d][%d][%llu]: %Lf\n",i,j,k,T_variable_phi_variable_a[i][j][k]);
			}
		}
	}

}

void printFixationsVsOutputCount(unsigned long long int ****fixations_vs_output_count)
{

unsigned long long int i=0;
unsigned long long int j=0;
unsigned long long int k=0;
unsigned long long int l=0;

unsigned long long int total_fixations = pow(2,NOFIB);
unsigned long long int total_outputs = pow(2,NOFOB);

	for(i = 0;i <=ROUND; i++)
	{
		for(j=1; j <= (4*n - NOFIB); j++)
		{
			for(k=0; k < total_fixations; k++ )
			{
				for(l = 0; l < total_outputs; l++)
				{
					//fixations_vs_output_count[i][j][k][l] = 0;
					printf("fixations_vs_output_count[%llu][%llu][%llu][%llu]:%llu\n",i,j,k,l,fixations_vs_output_count[i][j][k][l]);
				}
			}
		}
	}	

}


/*The following function is found online. I am just using it.*/
void print_time()
{
    time_t timer;
    char buffer[26];
    struct tm* tm_info;

    time(&timer);
    tm_info = localtime(&timer);

    strftime(buffer, 26, "%Y:%m:%d %H:%M:%S", tm_info);
    puts(buffer);
}

/* START START ===================================================================
long double*** prepareSSACapacities(unsigned long long int ***fixations_vs_output_count)
{
int i = 0;
unsigned long long int j = 0;
unsigned long long int total_fixations = pow(2,NOFIB);

	long double ***ssa_capacities = (long double ***)malloc(sizeof(long double*)*(ROUND+1));

	for(i = 0; i <= ROUND;i++)
	{
		ssa_capacities[i] = (long double **)malloc(sizeof(long double*)*total_fixations);
		for(j = 0; j < total_fixations; j++)
		{
			ssa_capacities[i][j] = (long double *)malloc(sizeof(long double)*2);

			//and initialize
			ssa_capacities[i][j][0] = -1; //we will store the experimental capacity here for round i and fixation j
			ssa_capacities[i][j][1] = -1; //we will store the theoretical capacity here for round i and fixation j
			ssa_capacities[i][j][0] = computeExperimentalSSACapacity(i,j,fixations_vs_output_count);
		}
	}

return ssa_capacities;
}

void releaseSSACapacitiesMemory(long double ***ssa_capacities)
{

	int i = 0;
	unsigned long long int j = 0;
	unsigned long long int total_fixations = pow(2,NOFIB);

	for(i = 0; i<=ROUND; i++)
	{	
		for(j=0; j < total_fixations; j++)
		{
			free(ssa_capacities[i][j]);
		}
		free(ssa_capacities[i]);
	}
	
	free(ssa_capacities);

}


long double computeExperimentalSSACapacity(int r,unsigned long long int a,unsigned long long int ***fixations_vs_output_count)
{

unsigned long long int eta = 0;
unsigned long long int total_outputs = pow(2,NOFOB);
unsigned long long int size_of_sample = pow(2,(4*n-NOFIB));
long double capacity_a = 0;

	for(eta = 0; eta < total_outputs; eta++)
	{
		capacity_a = capacity_a + pow((fixations_vs_output_count[r][a][eta]/(long double)size_of_sample - 1.0/total_outputs),2);
	}
	
	capacity_a = capacity_a*total_outputs;
	
	return capacity_a;
}



//The data type casting used while calculating the mean and variance needs to be checked closely. Could the be overflowed or truncated

long double*** computeMeanVariancePEta(unsigned long long int ***fixations_vs_output_count)
{
int r = 0;
unsigned long long a = 0; //fixations. Input bits of the trail
unsigned long long eta = 0; //$\eta$.  Output bits of the trail
unsigned long long int total_fixations = pow(2,NOFIB);
unsigned long long int total_outputs = pow(2,NOFOB);
long double mean = 0;
long double variance = 0;
unsigned long long int sum = 0;
unsigned long long int samplesize = pow(2,(4*n - NOFIB));

	long double ***mean_variance_p_eta = (long double ***)malloc(sizeof(long double**)*(ROUND+1));

	for(r = 0; r <= ROUND; r++)
	{
		mean_variance_p_eta[r] = (long double **)malloc(sizeof(long double*)*total_outputs);
		for(eta = 0;eta < total_outputs;eta++)
		{
			mean_variance_p_eta[r][eta] = (long double *)malloc(sizeof(long double)*2);
		}
	}


	// computing mean of $p_{\eta}(a)$ over all fixations a
	for(r = 1; r<= ROUND; r++)
	{
		for(eta = 0;eta < total_outputs; eta++)
		{
			sum = 0;
			for(a = 0; a < total_fixations; a++)
			{
				sum = sum + fixations_vs_output_count[r][a][eta];
			}
			mean = ((long double)sum/(long double)samplesize)/(long double)total_fixations;
			mean_variance_p_eta[r][eta][0] = mean;
		}
	}

	long double diff = 0;
	long double sum_for_variance = 0.0;
	// computing varaince of $p_{\eta}(a)$ over all fixations a
	for(r = 1; r<= ROUND; r++)
	{
		for(eta = 0;eta < total_outputs; eta++)
		{
			sum_for_variance = 0;
			for(a = 0; a < total_fixations; a++)
			{

				diff = (long double)fixations_vs_output_count[r][a][eta]/(long double)samplesize - mean_variance_p_eta[r][eta][0];
				sum_for_variance = sum_for_variance + pow(diff,2);
			}
			variance = sum_for_variance/total_fixations;
			mean_variance_p_eta[r][eta][1] = variance;
		}
	}

	return mean_variance_p_eta;
}


void releasecomputeMeanVariancePEtaMemory(long double ***mean_variance_p_eta)
{
	int i = 0;
	int j = 0;
	int total_outputs = pow(2,NOFOB);

	for(i = 0; i<=ROUND; i++)
	{	
		for(j=0; j < total_outputs; j++)
		{
			free(mean_variance_p_eta[i][j]);
		}
		free(mean_variance_p_eta[i]);
	}
	
	free(mean_variance_p_eta);
}



long double** computeSSACapacityTable(long double ***ssa_capacities)
{
int i = 0;
int a = 0;
unsigned long long int total_fixations = pow(2,NOFIB);
unsigned long long int total_outputs = pow(2,NOFOB);
long double **ssa_capacities_mean_variance_table = (long double **)malloc(sizeof(long double)*(ROUND+1));
long double sum = 0.0;
long double mean = 0.0;
long double experimental_variance = 0.0;

	for(i = 0;i <= ROUND; i++)
	{
		ssa_capacities_mean_variance_table[i] = (long double *)malloc(sizeof(long double)*3);

	}

	//computing average of $C(a)$ over all possible fixation a
	for(i = 0;i <= ROUND; i++)
	{
		sum = 0.0;
		for(a = 0; a < total_fixations; a++)
		{
			sum = sum + ssa_capacities[i][a][0];
		}

		mean = sum/(long double)total_fixations;
		ssa_capacities_mean_variance_table[i][0] = mean;
	}

	//computing varaince of $C(a)$ over all possible fixation a
	for(i = 0;i <= ROUND; i++)
	{
		sum = 0.0;
		for(a = 0; a < total_fixations; a++)
		{
			sum = sum + pow((ssa_capacities[i][a][0] - ssa_capacities_mean_variance_table[i][0]),2);
		}

		experimental_variance = sum/(long double)total_fixations;
		ssa_capacities_mean_variance_table[i][1] = experimental_variance;
		//now computing theoretical variance
		ssa_capacities_mean_variance_table[i][2] = 2*(pow(ssa_capacities_mean_variance_table[i][0],2))/((long double)total_outputs-1); 
	}

	return ssa_capacities_mean_variance_table;
}


void releasecomputeSSACapacityTableMemory(long double **ssa_capacities_mean_variance_table)
{

	int i =0;
	for(i = 0;i<=ROUND;i++)
	{
		free(ssa_capacities_mean_variance_table[i]);
	}

	free(ssa_capacities_mean_variance_table);

}


long double* computeVarianceVariancePEta(long double ***mean_variance_p_eta)
{
int i =0;
unsigned long int eta = 0;
unsigned long int total_outputs = pow(2,NOFOB);
long double sum = 0.0;
long double mean = 0.0;
long double variance = 0.0;

	long double *variance_variance_p_eta = (long double *)malloc(sizeof(long double)*(ROUND+1));
	
	for(i = 1;i <= ROUND; i++)
	{
		sum = 0;
		for(eta = 0; eta < total_outputs; eta++)
		{
			sum = sum + mean_variance_p_eta[i][eta][1];
		}
		mean = sum/(long double)total_outputs;

		sum = 0;
		for(eta = 0; eta < total_outputs; eta++)
		{
			sum = sum + pow((mean_variance_p_eta[i][eta][1] - mean),2);
		}
		variance = sum/(long double)total_outputs;
		variance_variance_p_eta[i] = variance;
	}
	
	return variance_variance_p_eta;
}

void releasecomputeVarianceVariancePEtaMemory(long double *variance_variance_p_eta)
{

	free(variance_variance_p_eta);
}


void printSSACapacityDetailTable(long double **ssa_capacities_mean_variance_table,long double *variance_variance_p_eta)
{
int i = 0;
long double distance = 0.0;
	//Start: temporary code
	printf("SSA Capacity Detail Table:\nRound	Avg_C_a	Exp_Vari_C_a	Theo_Var_C_a	Distance	var_var\n");
	for(i = 0;i <= ROUND;i++)
	{
		distance = fabs(ssa_capacities_mean_variance_table[i][1]-ssa_capacities_mean_variance_table[i][2]);
		printf("%d	%.8Lf	%.12Lf	%.12Lf	%.12Lf	%.15Lf\n",i,ssa_capacities_mean_variance_table[i][0],ssa_capacities_mean_variance_table[i][1],ssa_capacities_mean_variance_table[i][2],distance, variance_variance_p_eta[i]);
	}


}


END END =================================================================== */


long double*** prepareTphia(unsigned long long int ****fixations_vs_output_count)
{
	int i =0;
	unsigned long long int j = 0;
	unsigned long long int k = 0;
	unsigned long long int total_fixations = 0;

	total_fixations = pow(2,NOFIB);


	long double ***T_varaible_phi_varaible_a = (long double ***)malloc(sizeof(long double **)*(ROUND+1));

	for(i=0; i <= ROUND; i++)
	{
		T_varaible_phi_varaible_a[i] = (long double **)malloc(sizeof(long double*)*((4*n-NOFIB)+1));
		for(j=0; j <= (4*n-NOFIB); j++)
		{
				T_varaible_phi_varaible_a[i][j] = (long double *)malloc(sizeof(long double)*total_fixations);
		}
	}


	for(i=0; i <= ROUND; i++)
	{
		for(j=0; j <= (4*n-NOFIB); j++)
		{
			for(k = 0; k < total_fixations; k++)
			{
			//computing experimental value 
				T_varaible_phi_varaible_a[i][j][k] = computeTphia(i,j,k,fixations_vs_output_count);
			}
		}
	}

	return T_varaible_phi_varaible_a;
}


void releaseprepareTphiaMemory(long double ***T_varaible_phi_varaible_a)
{

int i = 0;
unsigned long long int a = 0;
unsigned long long int total_fixations = pow(2,NOFIB);

	for(i = 0;i<=ROUND;i++)
	{
		for(a = 0; a <= (4*n-NOFIB); a++)
		{
			free(T_varaible_phi_varaible_a[i][a]);
		}
		free(T_varaible_phi_varaible_a[i]);
	}
	free(T_varaible_phi_varaible_a);
}

long double computeTphia(int round, unsigned int phi_size, unsigned long long int fixation,unsigned long long int ****fixations_vs_output_count)
{
	unsigned long long int eta = 0;
	unsigned long long int total_outputs = 0;
	unsigned long long int samplesize = 0;
	long double T_a_phi = 0.0;
	long double x = 0.0,y = 0.0;
	total_outputs = pow(2,NOFOB);
	samplesize = pow(2,phi_size);
	eta = 0; x = 0; y = 0; T_a_phi = 0; 
	//printf("==========> =============> %Lf\n",T_a_phi);
	for(eta=0;eta < total_outputs; eta++)
	{
		x = (long double)fixations_vs_output_count[round][phi_size][fixation][eta] - (long double)samplesize*(1.0/total_outputs);
		y = (long double)samplesize*(1.0/total_outputs);
		T_a_phi = T_a_phi + pow(x,2)/y;
	}
	//printf("here is value of T_a_phi: %Lf\n",T_a_phi);
	
	return T_a_phi;
}


void preparePythonScriptForPlotting(long double ***T_variable_phi_variable_a)
{

    	char filename[100] = "";
	char roundstr[10];
	int round = 1;
	int j = 0;
	unsigned long long int i = 0;
	unsigned long long int total_fixations = pow(2,NOFIB);
	unsigned long long int total_outputs = pow(2,NOFOB);
	unsigned long long int maxsamplesize = pow(2,(4*n - NOFIB));
	FILE *f;

	for(round = 1;round <= ROUND; round++)
	{

		filename[0] = '\0';
		sprintf(roundstr, "%d", round);
		strcat(filename,"T_variable_a_variable_phi_increasing_size_round_");
		strcat(filename,roundstr);
		strcat(filename,".py");
			
		f = fopen(filename, "w");

		fprintf(f, "import numpy as np\nimport matplotlib.pyplot as plt\nimport math\n\n\n");

		fprintf(f,"t = [");
		
		//plot will start from samplesize 2^5 on x-axis
		for(j = 5; j < 4*n - NOFIB; j++)
		{
			fprintf(f,"%d,",j);

		}
		fprintf(f,"%d]\n\n\n",j);

		
		fprintf(f,"#Creating the list. Logorithm of sample size. Will be plotted in x-axis");
		for(i = 0; i < total_fixations;i++)
		{
			fprintf(f,"t_%llu = [",i);
			//plot will start from samplesize 2^5 on x-axis
			for(j = 5; j < 4*n - NOFIB; j++)
			{
				fprintf(f,"%Lf,",T_variable_phi_variable_a[round][j][i]);

			}
			fprintf(f,"%Lf]\n",T_variable_phi_variable_a[round][j][i]);

		}

		fprintf(f,"\n\n\n");
		//plot will start from samplesize 2^5 on x-axis

		fprintf(f,"#Below are the theoretical mean and variances of T for different sample sizes\n\n");
		for(j = 5; j <= 4*n - NOFIB; j++)
		{
			fprintf(f,"# sample sizeL %0.f\n",pow(2,j));
			fprintf(f,"mu_%.0f = %llu*(1-%.0f/%llu) + %.0f*xxxx\n",pow(2,j),total_outputs-1,pow(2,j),maxsamplesize,pow(2,j));
			fprintf(f,"sigma_%.0f = math.sqrt((2.0/%llu)*(%llu*(1-%.0f/%llu)+%0.f*xxxx)**2)\n",pow(2,j),total_outputs-1,total_outputs-1,pow(2,j),maxsamplesize,pow(2,j));
			fprintf(f,"\n\n");

		}


		fprintf(f,"#Plotting 5 different lines to present the theoretical distirbution of T\n\n");
		for(i = 0;i < 5; i++)
		{
			fprintf(f,"expected_T_a_%llu = []\n",i);
			for(j = 5;j <= 4*n - NOFIB; j++)
			{
				if(i == 0)
					fprintf(f,"expected_T_a_%llu.append(mu_%.0f)\n",i,pow(2,j));
				if(i == 1)
					fprintf(f,"expected_T_a_%llu.append(mu_%.0f+sigma_%.0f)\n",i,pow(2,j),pow(2,j));
				if(i == 2)
					fprintf(f,"expected_T_a_%llu.append(mu_%.0f-sigma_%.0f)\n",i,pow(2,j),pow(2,j));
				if(i == 3)
					fprintf(f,"expected_T_a_%llu.append(mu_%.0f+2*sigma_%.0f)\n",i,pow(2,j),pow(2,j));
				if(i == 4)
					fprintf(f,"expected_T_a_%llu.append(mu_%.0f-2*sigma_%.0f)\n",i,pow(2,j),pow(2,j));
			}
			fprintf(f,"plt.plot(t,expected_T_a_%llu,linewidth=.1, linestyle=%c-%c, c=%cDimGray%c)\n\n",i,'"','"','"','"');
		}

		fprintf(f,"#Plotting the experimental lines");
		for(i = 0;i < total_fixations; i++)
		{
			fprintf(f,"plt.plot(t, t_%llu, linewidth=.1, linestyle=%c-%c, c=%cred%c)\n",i,'"','"','"','"');
		}
	
		fprintf(f,"\n\n\n");

		fprintf(f,"#Shading the theoretical distribution region\n");
		fprintf(f,"plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha=.7)\n");
		fprintf(f,"plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha=.35)\n");
		fprintf(f,"plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha=.35)\n");


		fprintf(f,"\n\n#Formatting the plot\n\n");

		fprintf(f,"plt.ylabel('$T(\\phi,a)$')\n");
		fprintf(f,"plt.title('$T(\\phi,a)$ in SMALLPRESENT-4 with all zero key upto %d rounds')\n",round);
		fprintf(f,"plt.text(5.2,78,'For all $\\phi_1,\\phi_2$ if $|\\phi_1|=|\\phi_2|$ then $\\phi_1 = \\phi_2$')\n");
		fprintf(f,"plt.text(5.2,85,'For all $\\phi_1,\\phi_2$ if $|\\phi_1| < |\\phi_2|$ then $\\phi_1 \\subset \\phi_2$')\n");
		fprintf(f,"plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\\phi,a)$')\n");
		fprintf(f,"plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\\phi,a)$')\n");
		fprintf(f,"plt.axis([5, 12, 0, 120])\n");
		fprintf(f,"plt.grid(True)\n");
		fprintf(f,"plt.show()\n");

		fclose(f);
	}


}


/*START START ========================================================

long double ** prepareTphiaTable(long double ***T_variable_phi_variable_a,long double **ssa_capacities_mean_variance_table)
{
	int i =0;
	unsigned long long int j = 0;
	unsigned long long int total_fixations = pow(2,NOFIB);
	unsigned long long int total_outputs = pow(2,NOFOB);
	long double **T_phi_a_mean_variance_table = (long double **)malloc(sizeof(long double)*(ROUND+1));
	long double sum = 0.0;
	long double mean = 0.0;
	long double variance = 0.0;
	unsigned long long int samplesize = pow(2,(4*n-NOFIB));

	for(i = 0;i <= ROUND; i++)
	{
		T_phi_a_mean_variance_table[i] = (long double *)malloc(sizeof(long double)*4);

	}
	
	//Computing experimental and theoretical mean and variance
	for(i = 0;i <= ROUND; i++)
	{	

		//Computing mean
		sum = 0;
		for(j=0; j < total_fixations; j++)
		{
			sum = sum + (long double)T_variable_phi_variable_a[i][j][0];
		}
		mean = sum/(long double)total_fixations;
		T_phi_a_mean_variance_table[i][0] = mean; //experimental
		T_phi_a_mean_variance_table[i][1] = samplesize*ssa_capacities_mean_variance_table[i][0]; //theoretical

		//Computing variance
		sum = 0;
		for(j=0; j < total_fixations; j++)
		{
			sum = sum + pow(((long double)T_variable_phi_variable_a[i][j][0] - mean),2);
		}
		variance = sum/(long double)total_fixations;
		T_phi_a_mean_variance_table[i][2] = variance; //experimental
		T_phi_a_mean_variance_table[i][3] = 2*pow((samplesize*ssa_capacities_mean_variance_table[i][0]),2)/((long double)total_outputs-1); //theoretical
		
	}

	return T_phi_a_mean_variance_table;
}



void releaseprepareTphiaTableMemory(long double **T_phi_a_mean_variance_table)
{

int i = 0;

	for(i=0;i<=ROUND; i++)
	{
		free(T_phi_a_mean_variance_table[i]);
	}

	free(T_phi_a_mean_variance_table);

}



void print_T_phi_a_DetailTable(long double **T_phi_a_mean_variance_table,long double *variance_variance_p_eta)
{
int i = 0;
long double distance = 0.0;
	//Start: temporary code
	printf("T_a_phi Detail Table:\nRound	Exp_Avg_T_a_phi	Theo_Avg_T_a_phi	Exp_Var_T_a_phi	Theo_Var_T_a_phi	var_var_p_eta\n");
	for(i = 0;i <= ROUND;i++)
	{
		//distance = fabs(ssa_capacities_mean_variance_table[i][1]-ssa_capacities_mean_variance_table[i][2]);
		printf("%d	%.8Lf	%.12Lf	%.12Lf	%.12Lf	%.15Lf\n",i,T_phi_a_mean_variance_table[i][0],T_phi_a_mean_variance_table[i][1],T_phi_a_mean_variance_table[i][2],T_phi_a_mean_variance_table[i][3], variance_variance_p_eta[i]);
	}


}


END  END ======================================================== */
