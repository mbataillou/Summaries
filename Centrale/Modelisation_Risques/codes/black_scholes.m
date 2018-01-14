%----------------------------
%   IMPLANTATION DU CALL
%----------------------------
S_0=75;K=75;T=1;sigma=0.17;r=0.01;K_0=K*exp(-r*T);

d_pos=(log(S_0/K)+(r+sigma^2/2)*T)/(sigma*T^0.5);
d_neg=(log(S_0/K)+(r-sigma^2/2)*T)/(sigma*T^0.5);

CALL = S_0*normcdf(d_pos)-K_0*normcdf(d_neg);
PUT = -S_0*normcdf(-d_pos)+K_0*normcdf(-d_neg);

%----------------------------
%   CALL EN FONCTION DE S0
%----------------------------
CALL_S0=[];
S_list=1:0.5:150;
for i = 1:size(S_list,2)
    CALL_S0(i) = S_list(i) * normcdf((log(S_list(i)/K) + (r+(sigma^2)/2)*T) / (sigma*T^0.5)) - K_0 * normcdf((log(S_list(i)/K) + (r-(sigma^2)/2)*T) / (sigma*T^0.5));  
end
%----------------------------
%   CALL EN FONCTION DE SIGMA
%----------------------------
CALL_sigma=[];
sigma_list=0:1/1000:0.5;
for i = 1:size(sigma_list,2)
    CALL_sigma(i) = S_0 * normcdf((log(S_0/K) + (r+(sigma_list(i)^2)/2)*T) / (sigma_list(i) * (T^0.5))) - K_0 * normcdf((log(S_0/K) + (r-(sigma_list(i)^2)/2)*T) / (sigma_list(i)*(T^0.5)));  
end
%----------------------------
%   CALL EN FONCTION DE T
%----------------------------
CALL_t=[];
T_list=0:0.001:4;
for i = 1:size(T_list,2)
    CALL_t(i) = S_0*normcdf((log(S_0/K) + (r+(sigma^2)/2)*T_list(i)) / (sigma*(T_list(i))^0.5)) - K*exp(-r*T_list(i)) * normcdf( (log(S_0/K) + (r-(sigma^2)/2)*T_list(i)) / (sigma*(T_list(i))^0.5));  
end