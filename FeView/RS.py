import numpy as np
def resp_spectra(acc,dt, T_min=0.01, T_max=4, n_pts=200, Xi=0.05):
    Tn = np.logspace(np.log10(T_min), np.log10(T_max), n_pts)
    Wn = 2. * np.pi / Tn #Eq. 2.1.5, P. 41
    Wd = Wn * np.sqrt(1. - Xi**2.)# Eq. 2.2.5, P. 49
    #Table 5.2.1, P. 169
    A = np.exp(-Xi*Wn*dt)*(Xi/np.sqrt(1.-Xi**2.)*np.sin(Wd*dt)+np.cos(Wd*dt))
    B = np.exp(-Xi*Wn*dt)*(1./Wd*np.sin(Wd*dt))
    C = 1./Wn**2.*(2.*Xi/Wn/dt + np.exp(-Xi*Wn*dt)*(((1.-2.*Xi**2.)/Wd/dt-Xi/np.sqrt(1.-Xi**2.))*np.sin(Wd*dt) - (1+2.*Xi/Wn/dt)*np.cos(Wd*dt)))
    D = 1./Wn**2.*(1-2.*Xi/Wn/dt + np.exp(-Xi*Wn*dt)*((2.*Xi**2.-1)/Wd/dt*np.sin(Wd*dt)+2.*Xi/Wn/dt*np.cos(Wd*dt)))
    A_dash = -np.exp(-Xi*Wn*dt)*(Wn/np.sqrt(1.-Xi**2.)*np.sin(Wd*dt))
    B_dash = np.exp(-Xi*Wn*dt)*(np.cos(Wd*dt) - Xi/np.sqrt(1.-Xi**2.)*np.sin(Wd*dt))
    C_dash = 1./Wn**2.*(-1./dt + np.exp(-Xi*Wn*dt)*((Wn/np.sqrt(1.-Xi**2.)+Xi/dt/np.sqrt(1.-Xi**2.))*np.sin(Wd*dt)+1./dt*np.cos(Wd*dt)))
    D_dash = 1./Wn**2./dt*(1 - np.exp(-Xi*Wn*dt)*(Xi/np.sqrt(1.-Xi**2.)*np.sin(Wd*dt) + np.cos(Wd*dt)))
    SA = []; PSA=[]; SV=[]; PSV=[]; SD=[]
    for i in range(len(Tn)):
        u = np.zeros(len(acc))
        u_dot = np.zeros(len(acc))
        for j in range(len(acc) - 1):
            p= -1* acc[j]# p=-ma; m=1
            p_1=-1*acc[j + 1]
            u[j + 1] =A[i]*u[j]+B[i]*u_dot[j]+C[i]*p+D[i]*p_1 #Eq. 5.2.5a, P.168
            u_dot[j + 1] =A_dash[i]* u[j]+B_dash[i]*u_dot[j]+C_dash[i]*p+D_dash[i]*p_1 #Eq. 5.2.5b, P.168
        u_dot_dot = -(2. * Wn[i] * Xi * u_dot + Wn[i] ** 2. * u + acc)
        utdd_ = u_dot_dot + acc
        # Ch. 6
        SD.append((np.max(np.abs(u))))
        SV.append((np.max(np.abs(u_dot))))
        SA.append((np.max(np.abs(utdd_))))
        PSV.append((SD[i] * Wn[i]))
        PSA.append((SD[i] * Wn[i]**2))
    Fn=  1./Tn
    return Tn,Fn, SD,SV,SA,PSA,PSV