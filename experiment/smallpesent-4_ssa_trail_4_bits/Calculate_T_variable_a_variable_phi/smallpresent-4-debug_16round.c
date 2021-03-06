#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>

#define BLOCKLENGTH 16
#define KEYLENGTH 80
#define SAMPLESIZE 2048

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
float calculate_T_a(int fixation);
void process_T_a(int fixation,int samples);
void initializeDistributionforfixation(int fixation);

void applyRoundFunction(int r);
void addRoundKey(int r);
void applySBox(int r);
void applyPBox(int r);

int powOf2(int x);

int ROUND = 1;
unsigned char plaintext[40][BLOCKLENGTH/8];
unsigned char keys[40][KEYLENGTH/8];
int distribution[16][16];
int ssadistribution[16];
float mlcapacity[32][1]; //stores ml capacity for different rounds
float ssacapacity[32][16][1]; //stores sssa capacity for different rounds and different fixations
float T_a[16][10000];

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

int main()
{
	int i = 0,k=0,plaintexts=0,fixations=0;
	int trailoutput,samples=0;
	initializeDistribution();
	//initialize the master key
	keys[0][0] = 0x00; keys[0][1] = 0x00; keys[0][2] = 0x00; keys[0][3] = 0x00; keys[0][4] = 0x00;
	keys[0][5] = 0x00; keys[0][6] = 0x00; keys[0][7] = 0x00; keys[0][8] = 0x00; keys[0][9] = 0x00;	

	//printf("The key schedule is generated by the master key: 0x00 00 00 00 00 00 00 00 00 00\n-----------------------------------------------\n");
	ROUND = 32;
	generateRoundKeys();	
	ROUND = 1;

	srand ( time(NULL) ); //setting the seed of random number generator


	for(ROUND = 16;ROUND < 17; ROUND++)
	{
		initializeDistribution();
		for(fixations = 0;fixations < 16;fixations++)
		{

			for(samples = 0; samples < 10000; samples++)
			{

				initializeDistributionforfixation(fixations);
				

				initializessaDistribution();
				for(k = 0;k < SAMPLESIZE;k++)
				{
					//printRoundKeys();
					plaintexts = rand()%4096;
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
			
				//ssacapacity[ROUND][fixations][0] = calculatessacapacity();
				//printf("\tFor fixation %01x, the ssa capacity is: %f \n",fixations,calculatessacapacity());
				//printf("Sample: %d	Fixation: %d	T_a(phi): %f\n",samples,fixations,calculate_T_a(fixations));
				printf("%f\n", calculate_T_a(fixations)); 
				T_a[fixations][samples] = (float)calculate_T_a(fixations);
			}
			
			//process_T_a(fixations,10000);
		}

	//process_T_a(fixations,10000);	

	//printDistribution();
	//printProbabilityDistribution();
	mlcapacity[ROUND][0] = calculateCapacity();
	//printf("Capacity of ML distribution in case of %d rounds is: %f \n",ROUND, calculateCapacity());
	}
	//processmlcapacities(ROUND);
	//processssacapacities(ROUND);
	return 1;
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
	

void initializeDistributionforfixation(fixation)
{
int j=0;

		for(j=0;j < 16; j++)
		{
			distribution[fixation][j] = 0;	
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


float calculateCapacity()
{
	int i = 0,j=0;
	float capacity = 0;

	for(i = 0;i < 16; i++)
	{
		for(j=0;j < 16; j++)
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
			capacity  = capacity + (ssadistribution[i]/4096.0 - 1/16.0)*(ssadistribution[i]/4096.0 - 1/16.0);		
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
		printf("After %d Rounds: %f\n",i,mlcapacity[i][0]);
	}

}


void processssacapacities(int round)
{
int i = 0,j=0,k=0;
float mean = 0,variance = 0,sum=0;
	printf("SSA Capacities:\n");
	for(i=1;i < round;i++)
	{
		sum =0;
		printf("After %d round: ",i);
		for(j = 0;j < 16; j++) //for all fixations
		{
			sum = sum + ssacapacity[i][j][0];
		}
	
		mean = sum/16.0;
		printf("Mean: %f ",mean);

		sum = 0;
		for(j=0;j < 16;j++)
		{
			sum = sum + (ssacapacity[i][j][0] - mean)*(ssacapacity[i][j][0] - mean);
		}
		variance = sum/16.0;
		printf("Variance: %f	Theoretical Variance: %f",variance,(2*mean*mean)/15);
		printf("\n");
	}
}


void printProbabilityDistribution()
{
int i = 0,j=0;
float mean = 0,variance = 0,sum = 0;

	for(i = 0;i < 16; i++) //for all etas
	{
		sum =0;
		printf("%02x:	",i);
		for(j=0;j < 16;j++) //for all fixations
		{
			//printf("%.2f	",distribution[j][i]/4096.0);
			sum = sum + distribution[j][i]/4096.0;
		}
		mean = sum/16.0;
		printf("%.6f	",mean);
		sum = 0;
		for(j=0;j < 16;j++)
		{
			sum = sum + (distribution[j][i]/4096.0 - mean)*(distribution[j][i]/4096.0 - mean);
		}
		variance = sum/16.0;
		printf("%.6f",variance);
		printf("\n");
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

void process_T_a(fixation,samples)
{
int i=fixation,j=0;
float mean = 0.0,variance = 0.0,sum = 0.0;

/*printf("***************************** here I am: %.6f\n",T_a[0][0]);
printf("***************************** here I am: %.6f\n",T_a[0][1]);
printf("***************************** here I am: fixation: %d and samples %d\n",fixation,samples); */


	for(i=0; i<16; i++)
	{
		for(j=0;j < samples;j++) //for all samples
		{
			sum = sum + T_a[i][j];
			//printf("%.6f ",T_a[fixation][j]);
		}
	}
	mean = sum/(samples*16);

	printf("Fixation = %02x 	Mean of T_fixed_a_variable_phi is: %.6f	",i,mean);
	sum = 0.0;
	for(i=0; i<16; i++)
	{
		for(j=0;j < samples;j++)
		{
			sum = sum + (T_a[i][j] - mean)*(T_a[i][j] - mean);
		}
	}
	variance = sum/(samples*16);
	printf("Variance of T_fixed_a_variable_phi is: %.6f",variance);
	printf("\n");

}
