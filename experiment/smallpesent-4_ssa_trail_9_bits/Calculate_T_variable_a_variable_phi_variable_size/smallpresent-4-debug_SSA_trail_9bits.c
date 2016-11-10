#include<stdio.h>
#include<math.h>

#define BLOCKLENGTH 16
#define KEYLENGTH 80
//#define SAMPLESIZE 2048.0

void generateRoundKeys();
void printRoundKeys();
void rotateKey61bitLeft(int r);
void applySBoxOnKey(int r);
unsigned char sBox(unsigned char input);
void addRoundCounterOnKey(int r);
void printState(int r);
void prepareplaintext(int fixations,int plaintexts);
void printDistribution();
void initializeDistribution();
void initializessaDistribution();
float calculateCapacity();
float calculatessacapacity();
void processmlcapacities(int round);
void processssacapacities(int round);
void printProbabilityDistribution();
void process_p_eta_variance_over_fixations(int round);
void print_capacity_distance_variance_variances();
void process_T_a();
void process_T_a1();
float calculate_T_a(int fixation);
void print_T_a_summary();
void calculatefullscalecapacities();
void initializeDistribution_fixation_wise(int fixations);
void generate_random_order_sampleset();

void applyRoundFunction(int r);
void addRoundKey(int r);
void applySBox(int r);
void applyPBox(int r);

void process_T_a();
float calculate_T_a(int fixation);

int powOf2(int x);

int ROUND = 1;
unsigned char plaintext[40][BLOCKLENGTH/8];
unsigned char keys[40][KEYLENGTH/8];
int distribution[16][16];
int ssadistribution[16];
float mlcapacity[32][1]; //stores ml capacity for different rounds
float ssacapacity[32][16][1]; //stores sssa capacity for different rounds and different fixations
float p_eta_variance_over_fixations[32];
float variance_of_variances_of_p_eta[32];
float p_eta_means[32][16];
float p_eta_variances[32][16];
float ssacpacitysummary[32][4];
float T_a[32][16];
float T_a1[32][13][16];
float T_a_summary[32][4];
float SAMPLESIZE=4096.0;
int log_of_sample_size = 5;
int sample_plaintext_set[4096];


unsigned char sBox(unsigned char input)
{
	if(input == 0x00)
		return 0x0C;
	else if (input == 0x01)
		return 0x05;
	else if (input == 0x02)
		return 0x06;
	else if (input == 0x03)
		return 0x0B;
	else if (input == 0x04)
		return 0x09;
	else if (input == 0x05)
		return 0x00;
	else if (input == 0x06)
		return 0x0A;
	else if (input == 0x07)
		return 0x0D;
	else if (input == 0x08)
		return 0x03;
	else if (input == 0x09)
		return 0x0E;
	else if (input == 0x0A)
		return 0x0F;
	else if (input == 0x0B)
		return 0x08;
	else if (input == 0x0C)
		return 0x04;
	else if (input == 0x0D)
		return 0x07;
	else if (input == 0x0E)
		return 0x01;
	else if (input == 0x0F)
		return 0x02;
}

void addRoundCounterOnKey(int r)
{
	keys[r][2] = keys[r][2] ^ (r >> 1);
	keys[r][1] = keys[r][1] ^ (r << 7);
}

void applySBoxOnKey(int r)
{
	unsigned char input;
	input = keys[r][9] >> 4;
	keys[r][9] = (keys[r][9] & 0x0f) ^ (sBox(input) << 4);	
}

void rotateKey61bitLeft(int r)
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
	keys[r][6]= keys[r][6] ^ (keys[r-1][9] & 0x07) << 5;


	keys[r][7]=keys[r-1][9] >> 3;
	keys[r][7]= keys[r][7] ^ (keys[r-1][0] & 0x07) << 5;

	keys[r][8]=keys[r-1][0] >> 3;
	keys[r][8]= keys[r][8] ^ (keys[r-1][1] & 0x07) << 5;

	keys[r][9]=keys[r-1][1] >> 3;
	keys[r][9]= keys[r][9] ^ (keys[r-1][2] & 0x07) << 5;
}


//the following function considers the key in keys[0][i] to be the master key
void generateRoundKeys()
{
	int i = 1;
	int j = 1;
	for(i = 1; i <= ROUND; i++)
	{
		rotateKey61bitLeft(i);
		applySBoxOnKey(i);
		addRoundCounterOnKey(i);
	}
}

void printRoundKeys()
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


void printState(int r)
{
	int i = 0;
	//printf("Plaintext after %d round: ",r);
	for(i = (BLOCKLENGTH/8)-1; i >= 0; i--)
	{
		printf("%02X ",plaintext[r][i]);
	}
	printf("\n");		

}



void applyRoundFunction(int r)
{
	addRoundKey(r);
	applySBox(r);
	applyPBox(r);
}


void addRoundKey(int r)
{
	plaintext[r][0] = plaintext[r-1][0] ^ keys[r-1][2];
	plaintext[r][1] = plaintext[r-1][1] ^ keys[r-1][3];
}

void applySBox(int r)
{
	plaintext[r][0] = sBox(plaintext[r][0] & 0x0f) ^ (sBox((plaintext[r][0] & 0xf0) >> 4) << 4);
	plaintext[r][1] = sBox(plaintext[r][1] & 0x0f) ^ (sBox((plaintext[r][1] & 0xf0) >> 4) << 4);
}

void applyPBox(int r)
{
	
	unsigned char bit0,bit1,bit2,bit3,bit4,bit5,bit6,bit7;
	unsigned char byte0,byte1;

	//constructing byte0
	bit0 = plaintext[r][0] & 0x01;
	bit1 = (plaintext[r][0] & 0x10) >> 4;
	bit2 = plaintext[r][1] & 0x01;
	bit3 = (plaintext[r][1] & 0x10) >> 4;
	bit4 = (plaintext[r][0] & 0x02) >> 1;
	bit5 = (plaintext[r][0] & 0x20) >> 5;
	bit6 = (plaintext[r][1] & 0x02) >> 1;
	bit7 = (plaintext[r][1] & 0x20) >> 5;

	bit1 = bit1 << 1; bit2 = bit2 << 2; bit3 = bit3 << 3; 
	bit4 = bit4 << 4; bit5 = bit5 << 5; bit6 = bit6 << 6; bit7 = bit7 << 7;

	byte0 = bit0 ^ bit1 ^ bit2 ^ bit3 ^ bit4 ^ bit5 ^ bit6 ^ bit7;


	//constructing byte1
	bit0 = (plaintext[r][0] & 0x04) >> 2;
	bit1 = (plaintext[r][0] & 0x40) >> 6;
	bit2 = (plaintext[r][1] & 0x04) >> 2;
	bit3 = (plaintext[r][1] & 0x40) >> 6;
	bit4 = (plaintext[r][0] & 0x08) >> 3;
	bit5 = (plaintext[r][0] & 0x80) >> 7;
	bit6 = (plaintext[r][1] & 0x08) >> 3;
	bit7 = (plaintext[r][1] & 0x80) >> 7;

	bit1 = bit1 << 1; bit2 = bit2 << 2; bit3 = bit3 << 3; 
	bit4 = bit4 << 4; bit5 = bit5 << 5; bit6 = bit6 << 6; bit7 = bit7 << 7;

	byte1 = bit0 ^ bit1 ^ bit2 ^ bit3 ^ bit4 ^ bit5 ^ bit6 ^ bit7;

	plaintext[r][0] = byte0;
	plaintext[r][1] = byte1;
}


int powOf2(int x)
{
	int i = 0,y=1;
	for(i = 1;i <=x; i++)
	{
		y = y*2;
	}
	return y;
}


void prepareplaintext(int fixations,int plaintexts)
{
	plaintext[0][0] = 0;
	plaintext[0][1] = 0;

	plaintext[0][0] = plaintext[0][0] ^ ((fixations & 0x00000003) << 5);
	plaintext[0][1] = plaintext[0][1] ^ ((fixations & 0x0000000c) >> 1);

	plaintext[0][0] = plaintext[0][0] ^ (plaintexts & 0x0000001f);
	plaintext[0][0] = plaintext[0][0] ^ ((plaintexts & 0x00000020) << 2);

	plaintext[0][1] = plaintext[0][1] ^ ((plaintexts & 0x00000040) >> 6);
	plaintext[0][1] = plaintext[0][1] ^ (((plaintexts & 0x00000f80) >> 7) << 3);
}


int main()
{
	int i = 0,k=0,plaintexts=0,fixations=0;
	int trailoutput;
	initializeDistribution();
	//initialize the master key
	keys[0][0] = 0x00; keys[0][1] = 0x00; keys[0][2] = 0x00; keys[0][3] = 0x00; keys[0][4] = 0x00;
	keys[0][5] = 0x00; keys[0][6] = 0x00; keys[0][7] = 0x00; keys[0][8] = 0x00; keys[0][9] = 0x00;	

	//printf("The key schedule is generated by the master key: 0x00 00 00 00 00 00 00 00 00 00\n-----------------------------------------------\n");
	ROUND = 32;
	generateRoundKeys();	
	ROUND = 1;

	//srand(time(NULL));

	calculatefullscalecapacities();

	
	generate_random_order_sampleset();


	for(ROUND = 4;ROUND < 5; ROUND++)
	{
		
		initializeDistribution();
		for(fixations = 0;fixations < 16;fixations++)
		{
		   SAMPLESIZE = 16;
		   for(log_of_sample_size = 5;log_of_sample_size < 13;log_of_sample_size++)
		   {

			SAMPLESIZE = SAMPLESIZE*2;
	   		initializeDistribution_fixation_wise(fixations);
			initializessaDistribution();
			//for(plaintexts = 0;plaintexts < SAMPLESIZE;plaintexts++)
			for(k = 0;k < SAMPLESIZE;k++)
			{

				//plaintexts = rand()%4096;
				plaintexts = sample_plaintext_set[k];
				//printRoundKeys();
				prepareplaintext(fixations,plaintexts);
				//printf("Trail Bits: %d, Nontrailbits : %d, Plaintext :",fixations,plaintexts); printState(0);
				//printf("Plaintext :"); printState(0);
				for(i = 1; i <= ROUND; i++)
				{
					applyRoundFunction(i);
				}
				addRoundKey(ROUND+1);
				trailoutput = ((plaintext[ROUND+1][0] & 0x60) >> 5)^(((plaintext[ROUND+1][1] & 0x06) >> 1) << 2);
				distribution[fixations][trailoutput]++;
				ssadistribution[trailoutput]++;
				//printf("Ciphertext: "); printState(ROUND+1); printf("	Trailoutput is: %02x \n",trailoutput);
				//printf("-----------------------------------------------\n");
			}
			ssacapacity[ROUND][fixations][0] = calculatessacapacity();
			//printf("\tFor fixation %01x, the ssa capacity is: %f \n",fixations,calculatessacapacity());
			T_a[ROUND][fixations] = (float)calculate_T_a(fixations);
			T_a1[ROUND][log_of_sample_size][fixations] = (float)calculate_T_a(fixations);
		   }
		}	
	//printDistribution();
	
	printProbabilityDistribution();
	
	//process_T_a();
	process_T_a1();
	//printf("Capacity of ML distribution in case of %d rounds is: %f \n",ROUND, calculateCapacity());

	//printf("Testing:*************************** Mlcapacity %.12f\n",mlcapacity[14][0]);
	//printf("Testing:*************************** Mlcapacity %.12f\n",mlcapacity[15][0]);
	//printf("Testing:*************************** Mlcapacity %.12f\n",mlcapacity[16][0]);
	}
	processmlcapacities(ROUND); //pritns ml cpapacities
	processssacapacities(ROUND); 
	print_capacity_distance_variance_variances();
	print_T_a_summary();


	return 1;
}




void printDistribution()
{
int i = 0,j=0,sum = 0;
float mean = 0,variance = 0;

	for(i = 0;i < 16; i++) //for all fixations
	{
		sum =0;
		printf("%02x:	",i);
		for(j=0;j < 16;j++) //for all eta
		{
			printf("%d	",distribution[j][i]);
			sum = sum + distribution[j][i];
		}
		mean = sum/16.0;
		printf("%.2f	",mean);
		sum = 0;
		for(j=0;j < 16;j++)
		{
			sum = sum + (distribution[j][i] - mean)*(distribution[j][i] - mean);
		}
		variance = sum/16.0;
		printf("%.2f",variance);
		printf("\n");
	}
}


void initializessaDistribution()
{

int i = 0;

	for(i = 0;i < 16; i++)
	{
		ssadistribution[i] = 0;	
	}
}
	

void initializeDistribution()
{

int i = 0,j=0;

	for(i = 0;i < 16; i++)
	{
		for(j=0;j < 16; j++)
		{
			distribution[i][j] = 0;	
		}
	}
}

void initializeDistribution_fixation_wise(fixations)
{
int i = 0;

	for(i = 0;i < 16; i++)
	{
		distribution[fixations][i] = 0;	
	}

}


float calculateCapacity()
{
	int i = 0,j=0;
	float capacity = 0;

	for(i = 0;i < 16; i++)//for each fixation
	{
		for(j=0;j < 16; j++)//for each eta
		{
			capacity  = capacity + (distribution[i][j]/65536.0 - 1/256.0)*(distribution[i][j]/65536.0 - 1/256.0);	
			//capacity = capacity + (float)distribution[i][j]/65536.0;
		}
	}

	capacity = capacity * 256;
	return capacity;
}

float calculatessacapacity()
{
	int i = 0;
	float capacity=0;
	for(i = 0;i < 16; i++)
	{
			capacity  = capacity + (ssadistribution[i]/SAMPLESIZE - 1/16.0)*(ssadistribution[i]/SAMPLESIZE - 1/16.0);		
	}

	capacity = capacity * 16;

	return capacity;
}

void processmlcapacities(int round)
{
int i = 0;
	printf("ML Capacities:\n");
	for(i=1;i < round;i++)
	{
		printf("After %d Rounds: %.12f\n",i,mlcapacity[i][0]);
	}

}


void processssacapacities(int round)
{
int i = 0,j=0,k=0;
float mean = 0,variance = 0,sum=0;
	//printf("SSA Capacities:\n");
	for(i=1;i < round;i++)
	{
		sum =0;
		//printf("After %d round: ",i);
		for(j = 0;j < 16; j++) //for all fixations
		{
			sum = sum + ssacapacity[i][j][0];
		}
	
		mean = sum/16.0;
		//printf("Mean: %f ",mean);

		sum = 0;
		for(j=0;j < 16;j++)
		{
			sum = sum + (ssacapacity[i][j][0] - mean)*(ssacapacity[i][j][0] - mean);
		}
		variance = sum/16.0;
		ssacpacitysummary[i][0] = variance; //practical variance
		ssacpacitysummary[i][1] = (2*mean*mean)/15; //theoretical variance
		ssacpacitysummary[i][2] = ssacpacitysummary[i][0] - ssacpacitysummary[i][1]; //difference
		//printf("Variance: %.12f And Theoretical Variance: %.12f Difference: %.12f",variance,(2*mean*mean)/15,variance-(2*mean*mean)/15);
		//printf("Difference: %.10f, variance_of_variances_of_p_eta: %.12f",variance-(2*mean*mean)/15,variance_of_variances_of_p_eta_over_fixations[i]);
		//printf("\n");
	}
}


void printProbabilityDistribution()
{
int i = 0,j=0,k=0;
float mean = 0,variance = 0,sum = 0;

printf("Printing p_eta detail for Round:%d\n",ROUND);
	for(i = 0;i < 16; i++) //for all eta
	{
		sum =0;
		printf("Eta: %02x	",i);
		for(j=0;j < 16;j++) //for all fixations
		{
			//printf("%.2f	",distribution[j][i]/SAMPLESIZE.0);
			sum = sum + distribution[j][i]/SAMPLESIZE;
		}
		mean = sum/16.0;
		printf("mean: %f	",mean);
		p_eta_means[ROUND][i] = mean;
		sum = 0;
		for(j=0;j < 16;j++)
		{
			sum = sum + (distribution[j][i]/SAMPLESIZE - mean)*(distribution[j][i]/SAMPLESIZE - mean);
		}
		
		variance = sum/16.0;
		//printf("%.12f",variance);
		p_eta_variances[ROUND][i] = variance;
		printf("Practical Variance:%.12f %.12f Therorectical Variance: %.12f",p_eta_variances[ROUND][i],variance,mlcapacity[ROUND][0]/(15*16));
		printf("\n");
	}

	sum = 0;
	for(i = 0;i < 16; i++) //for all eta
	{
		sum = sum + p_eta_variances[ROUND][i];
	}
	printf("sum: %.12f	",sum);
	mean = sum/16.0;
	sum = 0;
	for(i=0;i < 16;i++)
	{
		sum = sum + (p_eta_variances[ROUND][i] - mean)*(p_eta_variances[ROUND][i] - mean);
	}

	variance_of_variances_of_p_eta[ROUND] = sum/16.0;
	printf("And mean and variance of variances are:%.12f	%.12f\n",mean,variance_of_variances_of_p_eta[ROUND]);
	
}


void print_capacity_distance_variance_variances()
{
int i=0,j=0,k=0;

	for(i=1;i<ROUND;i++)
	{
		printf("Round:%d pract c_a: %.12f theo c_a: %.12f diff c_a: %.12f Variance of variances:%.15f\n",i,ssacpacitysummary[i][0],ssacpacitysummary[i][1],fabs(ssacpacitysummary[i][2]),variance_of_variances_of_p_eta[i]);
		//printf("Round:%d diff c_a: %.12f Variance of variances:%.12f\n",i,fabs(ssacpacitysummary[i][2]),variance_of_variances_of_p_eta[i]);	
	}
}


float calculate_T_a(int fixation)
{
int eta=0;
	float T_a_phi = 0;

	for(eta=0;eta < 16; eta++)
	{
		T_a_phi = T_a_phi + (distribution[fixation][eta] - SAMPLESIZE*(1/16.0))*(distribution[fixation][eta] - SAMPLESIZE*(1/16.0))/(SAMPLESIZE*(1/16.0));
	}
	return T_a_phi;
}


void process_T_a()
{
int i=0,j=0;
float mean = 0.0,variance = 0.0,sum = 0.0;

printf("Printing T_a for different a for ROUND:%d\n",ROUND);
	for(i=0; i<16; i++) //for all fixations
	{
		sum = sum + T_a[ROUND][i];
		printf("Fixation a: %02x		T_a is:%.15f\n",i,T_a[ROUND][i]);
	}
	mean = sum/(16);

	T_a_summary[ROUND][0] = mean; //practical mean
	T_a_summary[ROUND][1] = SAMPLESIZE*mlcapacity[ROUND][0]; //theoretical mean
	//printf("Fixation = %02x 	Mean of T_fixed_a_variable_phi is: %.6f	",i,mean);
	sum = 0.0;
	for(i=0; i<16; i++) //for all fixations
	{
		sum = sum + (T_a[ROUND][i] - mean)*(T_a[ROUND][i] - mean);
	}

	variance = sum/(16);
	T_a_summary[ROUND][2] = variance; //practical variance
	T_a_summary[ROUND][3] = (2.0/15.0)*(SAMPLESIZE*mlcapacity[ROUND][0])*(SAMPLESIZE*mlcapacity[ROUND][0]); //theoretical variance
	//printf("Variance of T_fixed_a_variable_phi is: %.6f",variance);
	//printf("\n");
}


void process_T_a1()
{
int i=0,j=0,m=5;
float mean = 0.0,variance = 0.0,sum = 0.0;
float T_a1_mean[13],T_a1_variance[13];

printf("Printing T_a for different a for ROUND:%d for different sample sizes\n",ROUND);
	for(i=0; i < 16; i++) //for all fixations
	{
		printf("t_%01x = [",i);
		sum = 0.0;
		for(j = 5;j < 13;j++) // for all sample sizes
		{
			//printf("Fixation a: %02x	log of samplesize %d	T_a is:%.15f\n",i,j,T_a1[ROUND][j][i]);
			printf("%.4f",T_a1[ROUND][j][i]);
			if(j != 12)
				printf(",");
		}

		printf("]\n");
	}


	for(i=5; i < 13; i++) //for all sample sizes
	{
		sum = 0.0;
		for(j = 0;j < 16;j++) // for all fixations
		{
			sum = sum + T_a1[ROUND][i][j];
		}

		mean = sum/16.0;

		sum = 0.0;
		for(j = 0;j < 16;j++) // for all fixations
		{
			sum = sum + (T_a1[ROUND][i][j] - mean)*(T_a1[ROUND][i][j] - mean);
		}

		variance = sum/16.0;

		T_a1_mean[i] = mean;
		T_a1_variance[i] = variance;

	}

	printf("Means:\n");
	for(i=5; i < 13; i++) //for all sample sizes
	{
		printf("%.4f	",T_a1_mean[i]);

	}
	printf("\nVariances:\n");
	for(i=5; i < 13; i++) //for all sample sizes
	{
		printf("%.4f	",T_a1_variance[i]);

	}
}


void print_T_a_summary()
{
int i = 0;

printf("Printing the summary of T_a\n");
	for(i=0; i < 32; i++)
	{
		printf("Round: %d Exp mean: %.2f Theo mean: %.2f Exp variance: %.2f Theo variance: %.2f variance of variances: %.15f\n",i,T_a_summary[i][0],T_a_summary[i][1],T_a_summary[i][2],T_a_summary[i][3],variance_of_variances_of_p_eta[i]);
	}
}



void calculatefullscalecapacities()
{

int fixations,plaintexts,i,trailoutput;
float temp_SAMPLESIZE=SAMPLESIZE;
SAMPLESIZE=4096.0;
	for(ROUND = 1;ROUND < 32; ROUND++)
	{
		initializeDistribution();
		for(fixations = 0;fixations < 16;fixations++)
		{
			initializessaDistribution();
			for(plaintexts = 0;plaintexts < 4096;plaintexts++)
			{

				prepareplaintext(fixations,plaintexts);
				for(i = 1; i <= ROUND; i++)
				{
					applyRoundFunction(i);
				}
				addRoundKey(ROUND+1);
				trailoutput = ((plaintext[ROUND+1][0] & 0x60) >> 5)^(((plaintext[ROUND+1][1] & 0x06) >> 1) << 2);
				distribution[fixations][trailoutput]++;
			}
			ssacapacity[ROUND][fixations][0] = calculatessacapacity();
			T_a[ROUND][fixations] = (float)calculate_T_a(fixations);
		}	

		mlcapacity[ROUND][0] = calculateCapacity();
	}
SAMPLESIZE = temp_SAMPLESIZE;
}

void generate_random_order_sampleset()
{
int sample_plaintext_set_local[4096][2];
int i = 0,temp=0,j=0;
int size = 4096;

	for(i=0;i<size;i++)
	{

		sample_plaintext_set_local[i][0] = rand()%(size-1);
		sample_plaintext_set_local[i][1] = i;

	}

	for(i = 0;i < size; i++)
	{
		for(j=i+1; j < size; j++)
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

	for(i=0;i < size;i++)
	{

		sample_plaintext_set[i] = sample_plaintext_set_local[i][1];
		//printf("%d	",sample_plaintext_set_local[i][1]);

	}

}
