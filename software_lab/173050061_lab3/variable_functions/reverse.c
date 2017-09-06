#include<stdio.h>
#include<string.h>


void produce(int a)
{
	print("%d\n",a);
}


int main()
{

	char in[1000];
	int i,j,k;int yy=0;
	char out[1];
	int st,en=0,n;
	int flag=0;
	int dd = 0;
	i = 0;
	scanf("%d",&n);
	gets(out);
	flag=0;
	while(n--)
	{

		
		gets(in);
	flag = 0;
	st = strlen(in) - 1;
	en = strlen(in) - 1;
	i = 0;
	produce(st) ;
	while(st >= 0)
	{	
		i = 0;
		while(in[st] != 32)
		{

			if( st == -1)
			{
				flag = 1;
				break;
			}
			st--;
		}
		k = st+1;
		while(k <= en)
		{
			printf("%c",in[k]);
			k++;
		}
		st = st-1;
		en = st;
		if(flag == 0)
			printf(" ");printf(" ");

	}
	}
return 0;
}

