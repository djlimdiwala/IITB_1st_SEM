#include<stdio.h>
#include<string.h>


int main()
{

	char in[100];
	int i,j,k;
	char out[100] = {};
	int track_app[26];
 	int error = 0;
	i = 0;
	while(i < 26)
	{
		track_app[i] = 0;
		i++;		
	}
	scanf("%s",in);
	i = 0;k = 0;
	while(i < strlen(in))
	{
		j = in[i] - 97;
		
		if(in[i] < 97 || in[i] > 123)
		{
			error = 1;
		}
		else
		{		
			if(track_app[j] == 0)
			{
				out[k] = in[i];
				track_app[j] = 1;	
				k++;
			}
		}
		i++;	
	}
	printf("%s",out);
	if(error == 1)
		printf(" error");
	return 0;
}
