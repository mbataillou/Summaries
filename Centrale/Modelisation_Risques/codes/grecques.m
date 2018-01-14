%----------------------------
%        DONNÉES
%----------------------------
S_0 = 75; K = 75; T = 1; sigma = 0.17; R = 0.01; k2 = 80; k1 = 75;
%----------------------------
%   DELTA RISK REVERSAL
%----------------------------
DELTA_RR=[];
S_list=1:0.5:150;
for i = 1:size(S_list,2)
    DELTA_RR(i) = normcdf((log(S_list(i)/k1) + (R+(sigma^2/2))*T)/(sigma*sqrt(T))) - 1 - normcdf((log(S_list(i)/k2) + (R+(sigma^2/2))*T) / (sigma*sqrt(T)));   
end	
%----------------------------
%   GAMMA RISK REVERSAL
%----------------------------
	
GAMMA_RR=[];
S_list=1:0.5:150;
for i = 1:size(S_list,2)
    GAMMA_RR(i) = normpdf((log(S_list(i)/k1)+ (R+(sigma^2/2))*T)/ (sigma*sqrt(T))) / (S_list(i) *sigma * sqrt(T) ) - normpdf(( log(S_list(i)/k2)+ (R+(sigma^2/2))*T) / (sigma*sqrt(T)))/(S_list(i)*sigma*sqrt(T));
end
%----------------------------
%   VEGA RISK REVERSAL
%----------------------------
VEGA_RR=[];
S_list=1:0.5:150;
for i = 1:size(S_list,2)
    VEGA_RR(i) = normpdf((log(S_list(i)/k1) + (R+(sigma^2/2))*T) / (sigma*sqrt(T))) * S_list(i)* sqrt(T) - normpdf((log(S_list(i)/k2) + (R + (sigma^2/2)) * T) /(sigma*sqrt(T)))*S_list(i) * sqrt(T);
end
%----------------------------
%   THETA RISK REVERSAL
%----------------------------
THETA_RR=[];
S_list=1:0.5:150;
for i = 1:size(S_list,2)
    THETA_RR(i) = normpdf((log(S_list(i)/k1) +( R+ (sigma^2/2))*T) / (sigma*sqrt(T)))* S_list(i)*sigma / (2*sqrt(T)) + R*k1 * exp(-R*T) * (normcdf((log(S_list(i)/k1) + (R-(sigma^2/2))*T)/(sigma*sqrt(T)))-1) - normpdf((log(S_list(i)/k2) + (R+(sigma^2/2))*T) / (sigma*sqrt(T))) * S_list(i)*sigma / (2*sqrt(T))+ R*k2*exp(-R*T) * normcdf((log(S_list(i)/k2) + (R-(sigma^2/2))*T))/(sigma*sqrt(T));
end










