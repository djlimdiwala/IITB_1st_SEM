#include<stdio.h>
#include<string.h>


int main()
{

	int m;
	
	int i,j,k,max;
	max = 1;
 	int n[1000];
	scanf("%d",&m);
	i = 0;
	while(i < 1000)
	{
		n[i] = 0;
		i++;		
	}
	i = 0;
	while(i < m)
	{
		scanf("%d",&j);
		n[j-1]++;
		if(j > max)
		max = j;

		i++;
	}
	
	k = n[0];
	j = 0;
	i = 1;
	
	while(i < max)
	{

		if(k < n[i])
{
			k = n[i];
			j = i;
}
		i++;
	}

	printf("%d",j+1);
	return 0;
}
