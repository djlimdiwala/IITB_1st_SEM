


int main()
{

	char in[1000];
	int i,j,k;
	char out[1];
	int st,en,n;
	int flag = 0;
	i = 0;
	scanf("%d",&n);
	gets(out);
	while(n--)
	{

		
		gets(in);
	flag = 0;
	st = strlen(in) - 1;
	en = strlen(in) - 1;
	i = 0;
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
			printf(" ");

	}
	}
return 0;
}

