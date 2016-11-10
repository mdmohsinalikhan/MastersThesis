#ifndef CONFIGURATION
#define CONFIGURATION

#define n 8 //number of sBoxes
#define ROUND 10
#define MAXROUND 31 //this value is required to handle the size of the arrays during the SSA experiments.
#define KEYLENGTH 10 //is in byte
#define NOFIB 8 //No of Fixed input bits
#define NOFOB 8 //No of Fixed output bits

//defining the masterkey
#define KEYS00 0x00
#define KEYS01 0x00
#define KEYS02 0x00
#define KEYS03 0x00
#define KEYS04 0x00
#define KEYS05 0x00
#define KEYS06 0x00
#define KEYS07 0x00
#define KEYS08 0x00
#define KEYS09 0x00

//number of bytes or in other words, number of unsigned chars
#define BLOCKLENGTH ((n%2 == 0 ) ? (n/2):(n/2+1))

#endif

/*the followings functions are used for generating the round keys. 
This functions will be found in keyGenerationFunctions.c file */
unsigned char** generateRoundKeys();
void rotateKey61bitLeft(int r,unsigned char **keys);
void applySBoxOnKey(int r,unsigned char **keys);
void addRoundCounterOnKey(int r,unsigned char **keys);
void printRoundKeys(unsigned char **keys);
void releaseKeyMemory(unsigned char **states);
void printMasterKey(unsigned char **keys);

/*The following functions are basic ingredients of the cryptosystem. 
That is, the sbox and pbox. Thye are found in sboxpbox.c file */
unsigned char sBox(unsigned char input);

/*The following functions are for encryption and decryption. 
They are found in encryptionFunctions.c */
unsigned char **allocate_Memory_for_plaintext_or_ciphertext();
void printState(int r,unsigned char **states);
void encryption(unsigned char **plaintext_states,unsigned char **keys);
void addRoundKey(int r,unsigned char **plaintext_states,unsigned char **keys);
void applySBox(int r,unsigned char **plaintext_states);
void pbox(int r,unsigned char **plaintext_states);

//Memory releasing. These functions will be found in encryptionFunctions.c file
void releaseStateMemory(unsigned char **states);


//SSA related functions. These functions will be found in ssaPreparation.c file
void prepareplaintext(unsigned char **plaintext_states,unsigned int **trails,unsigned long long int fixation,unsigned long long int freebits);
unsigned int** preparingtheTrail();
void freeTrailMemory(unsigned int **trails);
void configureationConsistencyCheck();

//SSA experiment related functions. These functions will be found in ssaExperiment.c file
void SSA(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails);
unsigned long long int** countFixationVsOutput(unsigned char **plaintext_states, unsigned char **keys,unsigned int **trails);
void releasecountFixationVsOutputMemory(unsigned long long int **fixations_a_vs_output_eta_count);
