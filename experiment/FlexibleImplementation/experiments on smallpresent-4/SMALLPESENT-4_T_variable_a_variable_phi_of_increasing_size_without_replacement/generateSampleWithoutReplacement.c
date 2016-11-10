#include<stdio.h>
#include<stdlib.h>
#include "config.h"
#include<math.h>

unsigned long long int* generateSampleWithoutreplacement()
{
	unsigned long long int i = 0;
	unsigned long long int samplesize = pow(2,(4*n-NOFIB));
	/* This funciton will generate the whole codebook sample for each fixation.
	  And the sample will be generated in random order. The plan is to generate 'samplesize' number of random random numbers. 
	  Each random number gets an index which grows sequentially. Then sort the random numbers. Then the indices of the sorted 
          random numbers will be the random order of the sample we need */

	unsigned long long int **sample_plaintext_set_local = (unsigned long long int**)malloc(sizeof(unsigned long long int*)*samplesize);
	unsigned long long int *sample_plaintext_set = (unsigned long long int*)malloc(sizeof(unsigned long long int)*samplesize);

	srand(123);

	for(i = 0; i < samplesize; i++)
	{
		sample_plaintext_set_local[i] = (unsigned long long int*)malloc(sizeof(unsigned long long int)*2);
		sample_plaintext_set_local[i][0] = rand()%(samplesize-1);
		sample_plaintext_set_local[i][1] =  i;
	}

	printf("I have started my sort at :"); print_time();
	sort(sample_plaintext_set_local);


	for(i = 0; i < samplesize; i++)
	{
		sample_plaintext_set[i] = sample_plaintext_set_local[i][1];
		//printf("%llu, %llu \n",sample_plaintext_set_local[i][0],sample_plaintext_set_local[i][1]);
	}


	for(i = 0; i < samplesize; i++)
	{
		free(sample_plaintext_set_local[i]);
	}

	free(sample_plaintext_set_local);

	return sample_plaintext_set;
}

/*void sort(unsigned long long int **sample_plaintext_set_local)
{

	unsigned long long samplesize = pow(2,(4*n-NOFIB));
	unsigned long long int i = 0;
	unsigned long long int j = 0;
	unsigned long long int temp = 0;
	for(i = 0;i < samplesize; i++)
	{
		for(j=i+1; j < samplesize; j++)
		{
			if(sample_plaintext_set_local[i][0] >  sample_plaintext_set_local[j][0])
			{
				temp = sample_plaintext_set_local[i][0];
				sample_plaintext_set_local[i][0] = sample_plaintext_set_local[j][0];
				sample_plaintext_set_local[j][0] = temp;


				temp = sample_plaintext_set_local[i][1];
				sample_plaintext_set_local[i][1] = sample_plaintext_set_local[j][1];
				sample_plaintext_set_local[j][1] = temp;
			}
		}
	}

}*/

/*I didnt write the merge sort. I downloaded it.*/
void sort(unsigned long long int **sample_plaintext_set_local)
{
	unsigned long long int samplesize = pow(2,(4*n-NOFIB));
	unsigned long long int s = 0;
	unsigned long long int **temp = (unsigned long long int **)malloc(sizeof(unsigned long long int*)*samplesize);
	

	for(s = 0;s < samplesize; s++)
	{
		temp[s] = (unsigned long long int *)malloc(sizeof(unsigned long long int)*2);
	}


	partition(sample_plaintext_set_local,0,samplesize-1,temp);

	for(s = 0;s < samplesize; s++)
	{
		free(temp[s]);
	}
	free(temp);

}


void partition(unsigned long long int **sample_plaintext_set_local,unsigned long long int low,unsigned long long int high,unsigned long long int **temp)
{

    int mid;

    if(low<high){
         mid=(low+high)/2;
         partition(sample_plaintext_set_local,low,mid,temp);
         partition(sample_plaintext_set_local,mid+1,high,temp);
         mergeSort(sample_plaintext_set_local,low,mid,high,temp);
    }
}


void mergeSort(unsigned long long int **sample_plaintext_set_local,unsigned long long int low,unsigned long long int mid,unsigned long long int high,unsigned long long int **temp)
{
	unsigned long long int s = 0;
	unsigned long long int i,m,k,l;
	unsigned long long int samplesize = pow(2,(4*n-NOFIB));


	l=low;
	i=low;
	m=mid+1;

    while((l<=mid)&&(m<=high)){

         if(sample_plaintext_set_local[l][0]<=sample_plaintext_set_local[m][0]){
             temp[i][0]=sample_plaintext_set_local[l][0];
	     temp[i][1]=sample_plaintext_set_local[l][1];
             l++;
         }
         else{
             temp[i][0]=sample_plaintext_set_local[m][0];
             temp[i][1]=sample_plaintext_set_local[m][1];
             m++;
         }
         i++;
    }

    if(l>mid){
         for(k=m;k<=high;k++){
             temp[i][0]=sample_plaintext_set_local[k][0];
             temp[i][1]=sample_plaintext_set_local[k][1];
             i++;
         }
    }
    else{
         for(k=l;k<=mid;k++){
             temp[i][0]=sample_plaintext_set_local[k][0];
             temp[i][1]=sample_plaintext_set_local[k][1];
             i++;
         }
    }
   
    for(k=low;k<=high;k++){
         sample_plaintext_set_local[k][0]=temp[k][0];
         sample_plaintext_set_local[k][1]=temp[k][1];
    }
}
