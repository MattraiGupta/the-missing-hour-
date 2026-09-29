Cw='reading';Cv='worried';Cu='focused';C8='pre';C7='idle';C6='Diya';BZ='post';BY='neel';BX='marwan';BW='insiya';BV='mari';BU='ameera';BT='Georgia';BS=float;BR=enumerate;B0='smug';AV='name';AI=range;A3=.0;k='tired';Z=None;Y=max;T='id';S=False;P=True;M='';I=len;H=min;G=int;C9='CASE FILE NO. 17-4';CA='header';Ba='loading';Bb='envelope_wobble';Bc='envelope_fly';Bd='envelope_opening';Be='transition';Cx='tbc';B1='intro';Bf='divider';CB=Cv;CC='surprised';Bg=BT;B2='letter_reveal';AW='menu';B3='alpha';Cy='side';AX='letter_hold';B4='chapter2_ready';AY='act2_bus';AZ='act2_folder';B5='act2_card';Aa='envelope_idle';Ab='casefile';Ac='label';AJ='spacer';a=Cw;u='gameplay';g='x';b='size';c='y';W='body';O=Z;V='Courier New';R=1.;J='neutral';Q=C6;N=A3;K=S;F=P;import pygame as A,sys,os,random as U,math;A.init();Cz=A.image.load('baricon.png');A.display.set_icon(Cz);B,D=1280,720;Bh=S;AK=A.display.set_mode((B,D),A.RESIZABLE);E=A.Surface((B,D));A.display.set_caption('The Missing Hour');C_=0,0,0;CD=120,120,120;D0=A.font.SysFont(V,28,bold=F);Ad=A.font.SysFont(V,16);D1=A.font.SysFont(V,15);D2=A.font.SysFont(V,16);Bi=A.font.SysFont(Bg,48);D3=A.font.SysFont(V,20);B6=A.font.SysFont(V,16);B7=A.font.SysFont(Bg,26);CE=A.font.SysFont(V,16,bold=F);D4=A.font.SysFont(V,13);CF=A.font.SysFont(V,18);D5=A.font.SysFont(Bg,22);D6=A.font.SysFont(V,20,bold=F);CG=A.font.SysFont(V,19);CH=A.font.SysFont(V,16,bold=F);D7=A.font.SysFont(V,48,bold=F);B8=os.path.dirname(os.path.abspath(__file__))
def v(filename,size=O,alpha=K):
	B=filename
	try:D='convert_alpha'if alpha else'convert';C=getattr(A.image.load(os.path.join(B8,B)),D)();return A.transform.smoothscale(C,size)if size else C
	except Exception as E:print(f"Could not load {B}: {E}");return
l=v('logo.png',(480,480));CI=v('env.png',(900,563));CJ=v('letter.png',(480,570));CK=v('office.png',(1280,720));AL=v('bus.png',(1280,720));CL=v('folder.png',(1280,720),alpha=P);D8={A[T]:v(f"{A[T]}_card.png",(480,640),alpha=P)for A in[{T:BU},{T:BV},{T:BW},{T:BX},{T:BY}]};B9=v('dialogue_box.png',(1280,200),alpha=F);Bj,BA=900,563;Bk=320
def D9(f):
	try:
		B=A.image.load(os.path.join(B8,f)).convert_alpha()
		if B.get_height()>Bk:C=Bk/B.get_height();B=A.transform.smoothscale(B,(G(B.get_width()*C),Bk))
		return B
	except:return
w={};DA,DB=162,200
def DC(name):
	try:B=A.image.load(os.path.join(B8,f"{name}_photo.png")).convert_alpha();return A.transform.smoothscale(B,(DA,DB))
	except:return
DD={A:DC(A)for A in[BU,BV,BW,BX,BY]}
for CM in[J,'angry','sad',B0,'smiling','soft',k,CC]:w[CM]=D9(f"diya_{CM}.png")
for(DE,DF)in w.items():
	if not DF:w[DE]=w[J]
BB=K;h=N;BC=0;CN=90;A4=J;Ae=J;Dt=R;Du=R;Dv=.008;CO=[]
for _ in AI(50):CO.append({g:U.randint(0,B),c:U.randint(0,D),'speed':U.uniform(.2,1.),b:U.randint(1,2),B3:U.randint(30,90)})
CP=[]
for _ in AI(60):CP.append({g:U.randint(0,B),c:U.randint(0,D),'sx':U.uniform(-.3,.3),'sy':U.uniform(.1,.5),b:U.randint(1,2),B3:U.randint(20,60)})
x=0;BD=0;L=U.Random(42);Dw=[('CASE #17-4',L.randint(60,400),L.randint(60,160),L.randint(-18,18)),('MISSING',L.randint(500,900),L.randint(80,200),L.randint(-12,12)),('08:47 PM',L.randint(900,1180),L.randint(60,180),L.randint(-20,20)),('NO WITNESSES',L.randint(40,300),L.randint(500,640),L.randint(-15,15)),('[CLASSIFIED]',L.randint(700,1100),L.randint(480,640),L.randint(-22,22)),('THE GILT ROOM',L.randint(300,700),L.randint(560,680),L.randint(-10,10)),('REDACTED',L.randint(100,400),L.randint(280,420),L.randint(-25,25)),('11PM - MIDNIGHT',L.randint(750,1150),L.randint(300,440),L.randint(-14,14))];CQ=[{T:BU,AV:'Ameera'},{T:BV,AV:'Mari'},{T:BW,AV:'Insiya'},{T:BX,AV:'Marwan'},{T:BY,AV:'Neel'}];CR=[(O,'The office smells like cold coffee and old paper.',J),(O,'The clock on the wall reads 08:47 PM.',k),(Q,'Okay. Coat. Keys. Door. We are leaving.',k),(O,"She'd been saying that for forty minutes.",J),(O,"That's when she saw it. An envelope. Dark red wax seal. No return address.",J),(O,'Just three words written carefully across the front: FOR THE DETECTIVE.',J),(Q,"...I don't see it.",k),(O,'She saw it.',J),(O,'She stood there for a full thirty seconds. Then sat back down, still in her coat.',k),(Q,"One look. That's it.",k),(O,'She told herself that too.',J),(O,'One page. Almost empty. Five witnesses. One missing hour.',a),(O,'Nobody remembers anything — word for word, every statement identical:',a),(O,'"I don\'t remember."',a),(Q,'...That makes no sense.',CC),(O,'She read it a third time.',a),(O,'She told herself she was just organizing. Not investigating. Just. Organizing.',J),(O,'The fifth folder disagreed.',J)];DG=[(Q,'Rayan Malik. Twenty-four. No signs of struggle. No explanation.',a),(O,'She closed the file. Opened it again.',J),(Q,'I hate this job.','sad'),(O,'She said it the way people say "I love this job."',J),(Q,'Ameera, Mari, Insiya, Marwan, Neel.',a),(Q,'One of them knows something.',B0),(O,'The office feels different now. Heavier.',J),(Q,'What really happened at that party?',CB),(O,'At some point she stopped arguing with herself and just put her coat on.',k),(O,'The files came with her.',J),(O,'Obviously.',J),(O,'The office light clicked off behind her.',J)];BE='A';d=0;A5=N;Af=M;A6=K;Bl=0;Bm=1.2
def BF():return CR if BE=='A'else DG
y=C7;e=R
def Bn(emotion):
	B=emotion;global A4,Ae,y,e;C={k:k,Cw:a,'thinking':Cy,Cu:a,Cv:CB};A=C.get(B,B)
	if A not in w:A=J
	if Ae!=A:
		Ae=A
		if h<.05:A4=A;y=C7;e=R
		else:y='out'
def Bo():
	global A4,Ae,y,e
	if y=='out':
		e=Y(N,e-.07)
		if e<=N:A4=Ae;y='in';e=N
	elif y=='in':
		e=H(R,e+.07)
		if e>=R:y=C7;e=R
def DH(surf):
	global x,BD
	for C in CP:
		F=A.Surface((C[b]*2,C[b]*2),A.SRCALPHA);A.draw.circle(F,(200,190,170,C[B3]),(C[b],C[b]),C[b]);surf.blit(F,(G(C[g]),G(C[c])));C[g]+=C['sx'];C[c]+=C['sy']
		if C[g]<-20:C[g]=B+20
		if C[g]>B+20:C[g]=-20
		if C[c]>D:C[c]=-20
		if C[c]<-20:C[c]=D
	BD+=1
	if BD>U.randint(60,180):BD=0;x=U.randint(-15,5)
	else:x=Y(0,x*.95)
	if x:
		E=A.Surface((B,D),A.SRCALPHA)
		if x>0:E.fill((255,245,220,x))
		else:E.fill((0,0,0,-x))
		surf.blit(E,(0,0))
def DI(surface):
	C=surface
	for L in AI(0,D,3):E=A.Surface((B,1),A.SRCALPHA);E.fill((0,0,0,22));C.blit(E,(0,L))
	F=A.Surface((B,D),A.SRCALPHA)
	for I in AI(720,0,-16):M=H(255,Y(0,G((720-I)*.42)));A.draw.circle(F,(0,0,0,M),(B//2,D//2),I)
	C.blit(F,(0,0));J=A.Surface((B,120),A.SRCALPHA)
	for K in AI(60):N=G(8*(1-abs(K-30)/30));J.fill((180,160,110,N),(0,K,B,1))
	C.blit(J,(0,D//2-60))
def DJ(surface,scale,mouse_pos,game_state_val,darkness_val):
	L=scale;C=surface;E=G(220*L);H=G(50*L);M=B//2-E//2;I=596;D=A.Rect(M,I,E,H);O=D.collidepoint(mouse_pos)
	if O:A.draw.rect(C,(18,14,8),D);A.draw.rect(C,(255,255,255),D,2);N=255,255,255
	else:A.draw.rect(C,(8,6,3),D);A.draw.rect(C,(200,200,200),D,1);N=210,210,210
	J=D0.render('START CASE',F,N);C.blit(J,(M+(E-J.get_width())//2,I+(H-J.get_height())//2))
	if game_state_val==AW:P=80+math.sin(A.time.get_ticks()*.003)*40;K=Ad.render('[ click to begin your investigation ]',F,(100,90,80));K.set_alpha(G(P));C.blit(K,(B//2-K.get_width()//2,I+H+20))
	return D
Ag=0;A7=0;A8=N;AM=K;DK=1.5;Ah=[(CA,C9),(Bf,M),(Ac,'SUBJECT'),(W,'Rayan Malik, 24.'),(AJ,M),(Ac,'INCIDENT'),(W,'Reported missing following a birthday gathering'),(W,'at rooftop venue: The Gilt Room.'),(W,'Last seen between 11 PM and midnight.'),(AJ,M),(Ac,'FINDINGS'),(W,'No signs of struggle.'),(W,'No witnesses.'),(W,'No explanation.'),(AJ,M),(Ac,'WITNESS STATEMENTS  [x5]'),(W,'Ameera  -  "I don\'t remember."'),(W,'Mari    -  "I don\'t remember."'),(W,'Insiya  -  "I don\'t remember."'),(W,'Marwan  -  "I don\'t remember."'),(W,'Neel    -  "I don\'t remember."'),(AJ,M),('note','[ click to continue ]')];AN=[];AO=M
def CS(text,font,max_width):
	E=text.split(' ');B=[];A=M
	for C in E:
		D=A+(' 'if A else M)+C
		if font.size(D)[0]<=max_width:A=D
		else:
			if A:B.append(A)
			A=C
	if A:B.append(A)
	return B
def DL(surface,alpha,revealed,current_str,done):
	V=current_str;L=alpha;G=surface;I,J=820,620;O=B//2-I//2;R=D//2-J//2;M=A.Surface((I,J),A.SRCALPHA);M.fill((30,22,13,248));X=A.Surface((I-20,J-20),A.SRCALPHA);X.fill((38,28,16,60));M.blit(X,(10,10));A.draw.rect(M,(115,90,52),(0,0,I,J),2);A.draw.rect(M,(75,60,35),(5,5,I-10,J-10),1);A.draw.rect(M,(55,42,24),(8,8,I-16,J-16),1)
	for(Y,Z)in[(14,14),(I-14,14),(14,J-14),(I-14,J-14)]:A.draw.circle(M,(100,78,44),(Y,Z),4,1)
	M.set_alpha(L);G.blit(M,(O,R));E=R+36;P=52;a=revealed+([V]if V else[])
	for(b,(N,Q))in BR(zip([A for(A,B)in Ah],a)):
		if N==CA:C=D6.render(Q,F,(185,158,112));C.set_alpha(L);G.blit(C,(B//2-C.get_width()//2,E));E+=36
		elif N==Bf:S=A.Surface((I-P*2,1));S.fill((85,68,46));S.set_alpha(L);G.blit(S,(O+P,E));E+=20
		elif N==Ac:T=A.Surface((3,18),A.SRCALPHA);T.fill((140,108,58,200));T.set_alpha(L);G.blit(T,(O+P-8,E+2));C=CH.render(Q,F,(148,118,72));C.set_alpha(L);G.blit(C,(O+P,E));E+=26
		elif N==W:C=CG.render(Q,F,(215,200,170));C.set_alpha(L);G.blit(C,(O+P+16,E));E+=28
		elif N==AJ:E+=14
		elif N=='note':
			if done and A.time.get_ticks()//500%2==0:C=CG.render(Q,F,(140,115,75));C.set_alpha(L);G.blit(C,(B//2-C.get_width()//2,E))
	if done:U=D7.render('UNSOLVED',F,(140,40,40));U.set_alpha(H(L,175));K=U.get_rect(center=(B//2+180,R+J-80));G.blit(U,K);A.draw.rect(G,(140,40,40),(K.x-6,K.y-4,K.width+12,K.height+8),2);A.draw.rect(G,(100,25,25),(K.x-10,K.y-8,K.width+20,K.height+16),1)
def DM(surface,timer):
	I=timer;C=surface;C.fill((8,6,4));e=G(I*1.4%(B+400))-200;W=A.Surface((200,D),A.SRCALPHA)
	for O in AI(200):P=G(5*(1-abs(O-100)/100));A.draw.line(W,(200,175,120,P),(O,0),(O,D))
	C.blit(W,(e,0));X=A.Surface((B,D),A.SRCALPHA)
	for Z in AI(600,0,-25):P=Y(0,G((600-Z)*.22));A.draw.circle(X,(0,0,0,P),(B//2,D//2),Z)
	C.blit(X,(0,0));L,J=B//2,D//2
	for f in[J-155,J+155]:a=A.Surface((560,1),A.SRCALPHA);a.fill((110,88,52,H(180,I*3)));C.blit(a,(L-280,f))
	g=H(255,Y(0,(I-10)*5));Q=CH.render('C A S E  F I L E  -  A C T  T W O',F,(120,95,58));Q.set_alpha(g);C.blit(Q,(L-Q.get_width()//2,J-128));h=H(255,Y(0,(I-25)*6));R=Bi.render('The Investigation Begins',F,(210,195,165));R.set_alpha(h);C.blit(R,(L-R.get_width()//2,J-86));i=H(160,Y(0,(I-40)*5));b=A.Surface((400,1),A.SRCALPHA);b.fill((100,80,50,i));C.blit(b,(L-200,J+20));j=H(255,Y(0,(I-45)*5));S=B6.render('The bus ride. Five witnesses. One missing hour.',F,(100,88,68));S.set_alpha(j);C.blit(S,(L-S.get_width()//2,J+34));N=H(255,Y(0,(I-65)*6));E,K=220,48;T,U=L-E//2,J+78;M=A.Surface((E,K),A.SRCALPHA);k=A.Rect(T,U,E,K).collidepoint(A.mouse.get_pos())
	if k:A.draw.rect(M,(60,50,35,220),(0,0,E,K),border_radius=3);A.draw.rect(M,(180,150,90,N),(0,0,E,K),2,border_radius=3);c=220,195,140
	else:A.draw.rect(M,(25,20,14,200),(0,0,E,K),border_radius=3);A.draw.rect(M,(100,82,52,N),(0,0,E,K),1,border_radius=3);c=150,128,90
	M.set_alpha(N);C.blit(M,(T,U));V=B6.render('C O N T I N U E',F,c);d=V.copy();d.set_alpha(N);C.blit(d,(T+E//2-V.get_width()//2,U+K//2-V.get_height()//2))
def act3_draw(surface,timer):
	I=timer;C=surface;C.fill((8,6,4));e=G(I*1.4%(B+400))-200;W=A.Surface((200,D),A.SRCALPHA)
	for O in AI(200):P=G(5*(1-abs(O-100)/100));A.draw.line(W,(200,175,120,P),(O,0),(O,D))
	C.blit(W,(e,0));X=A.Surface((B,D),A.SRCALPHA)
	for Z in AI(600,0,-25):P=Y(0,G((600-Z)*.22));A.draw.circle(X,(0,0,0,P),(B//2,D//2),Z)
	C.blit(X,(0,0));L,J=B//2,D//2
	for f in[J-155,J+155]:a=A.Surface((560,1),A.SRCALPHA);a.fill((110,88,52,H(180,I*3)));C.blit(a,(L-280,f))
	g=H(255,Y(0,(I-10)*5));Q=CH.render('C A S E  F I L E  -  A C T  T H R E E',F,(120,95,58));Q.set_alpha(g);C.blit(Q,(L-Q.get_width()//2,J-128))
	h=H(255,Y(0,(I-25)*6));R=Bi.render('The Interrogations',F,(210,195,165));R.set_alpha(h);C.blit(R,(L-R.get_width()//2,J-86))
	i=H(160,Y(0,(I-40)*5));b=A.Surface((400,1),A.SRCALPHA);b.fill((100,80,50,i));C.blit(b,(L-200,J+20))
	j=H(255,Y(0,(I-45)*5));S=B6.render('Nobody remembers anything. Someone is lying.',F,(100,88,68));S.set_alpha(j);C.blit(S,(L-S.get_width()//2,J+34))
	N=H(255,Y(0,(I-65)*6));E,K=220,48;T,U=L-E//2,J+78;M=A.Surface((E,K),A.SRCALPHA);k=A.Rect(T,U,E,K).collidepoint(A.mouse.get_pos())
	if k:A.draw.rect(M,(60,50,35,220),(0,0,E,K),border_radius=3);A.draw.rect(M,(180,150,90,N),(0,0,E,K),2,border_radius=3);c=220,195,140
	else:A.draw.rect(M,(25,20,14,200),(0,0,E,K),border_radius=3);A.draw.rect(M,(100,82,52,N),(0,0,E,K),1,border_radius=3);c=150,128,90
	M.set_alpha(N);C.blit(M,(T,U));V=B6.render('C O N T I N U E',F,c);d=V.copy();d.set_alpha(N);C.blit(d,(T+E//2-V.get_width()//2,U+K//2-V.get_height()//2))
def DN(surface,alpha,bar_progress,dot_index):
	D=alpha;C=surface;E=B//2;I=B6.render(C9,F,(74,69,64));I.set_alpha(D);C.blit(I,(E-I.get_width()//2,190));H=A.Surface((500,1));H.fill((42,37,32));H.set_alpha(D);C.blit(H,(E-250,214));J=Bi.render('Downtown Office',F,(200,191,176));J.set_alpha(D);C.blit(J,(E-J.get_width()//2,226));K=D3.render('0 8 : 4 7   P M',F,(90,82,72));K.set_alpha(D);C.blit(K,(E-K.get_width()//2,292));C.blit(H,(E-250,326));L=A.Surface((Ch,2));L.fill((42,37,32));L.set_alpha(D);C.blit(L,(Ci,BL));O=G(Ch*bar_progress)
	if O>0:M=A.Surface((O,2));M.fill((107,95,82));M.set_alpha(D);C.blit(M,(Ci,BL))
	P=[(58,53,48)]*3;P[dot_index]=107,95,82
	for(R,S)in BR(P):Q=A.Surface((8,8),A.SRCALPHA);A.draw.circle(Q,(*S,D),(4,4),4);C.blit(Q,(E-20+R*20,BL+22))
	N=D2.render('L O A D I N G . . .',F,(58,53,48));N.set_alpha(D);C.blit(N,(E-N.get_width()//2,BL+44))
def DO(surface,alpha):
	E=alpha;G=surface;K=BF()
	if d>=I(K):return
	L=K[d][0];Q,C,H=200,D-200,28
	if B9:M=B9.copy();M.set_alpha(E);G.blit(M,(0,C))
	if L:N=CE.render(L.upper(),F,(180,155,110));N.set_alpha(E);G.blit(N,(H,C+8));O=C+52
	else:O=C+48
	for(R,S)in BR(CS(Af,B7,B-H*2)[:3]):P=B7.render(S,F,(220,210,195));P.set_alpha(E);G.blit(P,(H,O+R*36))
	if A6 and A.time.get_ticks()//500%2==0:J=Ad.render('>',F,(140,115,75));J.set_alpha(E);G.blit(J,(B-H-J.get_width(),C+Q-28))
def DP(surface,hovered):B=surface;D=(160,140,120)if hovered else(80,70,60);A.draw.rect(B,(12,10,8),AG);A.draw.rect(B,D,AG,1);C=D4.render('SKIP >>',F,D);B.blit(C,(AG.x+(AG.width-C.get_width())//2,AG.y+(AG.height-C.get_height())//2))
def DQ(surface,typed_text,confirm_done,yes_hovered,no_hovered):
	C=surface;K=A.Surface((B,D),A.SRCALPHA);K.fill((0,0,0,180));C.blit(K,(0,0));E,G=560,160;L,H=B//2-E//2,D//2-G//2;A.draw.rect(C,(12,10,8),(L,H,E,G));A.draw.rect(C,(80,70,60),(L,H,E,G),1);M=D5.render(typed_text,F,(200,190,175));C.blit(M,(B//2-M.get_width()//2,H+36))
	if confirm_done:N=(200,80,80)if yes_hovered else(120,60,60);O=(160,140,120)if no_hovered else(80,70,60);A.draw.rect(C,(12,10,8),A1);A.draw.rect(C,N,A1,1);I=CF.render('LEAVE',F,N);C.blit(I,(A1.x+(A1.width-I.get_width())//2,A1.y+(A1.height-I.get_height())//2));A.draw.rect(C,(12,10,8),A2);A.draw.rect(C,O,A2,1);J=CF.render('STAY',F,O);C.blit(J,(A2.x+(A2.width-J.get_width())//2,A2.y+(A2.height-J.get_height())//2))
def DR(surface,alpha):
	if not CJ:return
	A=CJ.copy();A.set_alpha(alpha);surface.blit(A,(B//2-A.get_width()//2,D//2-A.get_height()//2))
def CT():E,F=AK.get_size();C=H(E/B,F/D);I,J=G(B*C),G(D*C);K,L=(E-I)//2,(F-J)//2;M,N=A.mouse.get_pos();return G((M-K)/C),G((N-L)/C)
Ai=0;BG=0;CU=160;Aj=S;DS=0;AP=C8;A9=[(Z,'Rain streaks the bus windows.',J),(Z,'The city passes in blurred gold and gray outside.',J),(Z,'She rereads the file for the third time.',J),(Q,'Same page. Same names. Same silence.',a),(Q,'Five people in the same place at the same time — and not one of them remembers anything.',a),(Z,'She stares at that for a long moment.',J),(Q,"That doesn't happen by accident.",Cu),(Z,'She opens the folder.',a)];AA=[(Z,'She closes the folder.',J),(Z,'The bus hums. Rain taps the glass.',J),(Q,'...All five of them. Same answer. Word for word.',a),(Q,"That's not a coincidence.",Cu),(Z,'She checks the time.',J),(Q,'10:47. I have until midnight.',k),(Q,'One hour. Five witnesses. One of them will crack.',B0),(Z,'The bus stops.',J),(Q,"...Let's go.",J)];m=0;AB=A3;Ak=M;AC=S;CV=S;n=0;AD=A3;Al=M;AE=S;CW=S;i=0;AQ=A3;CX=60;DT=S;Am=set();BH=Z;AR=0;Bp=S;Dx=A.font.SysFont(BT,18,italic=P);Dy=A.font.SysFont(BT,15,italic=P)
try:CY=A.font.Font(os.path.join(B8,'amsterdam.ttf'),42)
except:CY=A.font.SysFont(BT,42,italic=P)
DU=CY;z=0;B4b='act3_ready';act3t=0
def CZ(surface,alpha,text,speaker,done):
	I=speaker;F=alpha;E=surface
	if not text:return
	N,C,G=200,D-200,28
	if B9:J=B9.copy();J.set_alpha(F);E.blit(J,(0,C))
	if I:K=CE.render(I.upper(),P,(180,155,110));K.set_alpha(F);E.blit(K,(G,C+8));L=C+52
	else:L=C+48
	for(O,Q)in BR(CS(text,B7,B-G*2)[:3]):M=B7.render(Q,P,(220,210,195));M.set_alpha(F);E.blit(M,(G,L+O*36))
	if done and A.time.get_ticks()//500%2==0:H=Ad.render('>',P,(140,115,75));H.set_alpha(F);E.blit(H,(B-G-H.get_width(),C+N-28))
def Ca():A=G(AQ);B=[(BU,175,A+210),(BV,175,A+320),(BW,175,A+430),(BX,780,A+240),(BY,780,A+370)];return B
def Cb(surface):
	C=surface;global i
	if AL:C.blit(AL,(0,0))
	else:C.fill((8,6,4))
	if CL:M=CL.copy();M.set_alpha(i);C.blit(M,(0,G(AQ)))
	V=Ca();W,X=CT()
	for(N,J,K)in V:
		L=N in Am;O=(60,38,18)if L else(80,55,30);Y=A.Rect(J-10,K-8,240,42).collidepoint(W,X)
		if Y and not L:O=255,235,180
		Z=next(A[AV]for A in CQ if A[T]==N);F=DU.render(Z,P,O);F.set_alpha(i);C.blit(F,(J,K))
		if L:a=K+F.get_height()//2+2;Q=A.Surface((F.get_width(),2),A.SRCALPHA);Q.fill((90,65,35,G(i)));C.blit(Q,(J,a))
	R=D-48
	if I(Am)==5:S='[ all files reviewed — click to continue ]';U=180,155,100
	else:S=f"[ {I(Am)}/5 files reviewed ]";U=160,138,90
	E=B6.render(S,P,U);H=A.Surface((E.get_width()+24,E.get_height()+10),A.SRCALPHA);H.fill((0,0,0,160));H.set_alpha(i);C.blit(H,(B//2-H.get_width()//2,R-4));E.set_alpha(i);C.blit(E,(B//2-E.get_width()//2,R))
def DV(surface,suspect,alpha):
	H=suspect;E=surface;C=alpha;I=D8.get(H[T])
	if not I:return
	J=B//2-240;F=D//2-320;K=I.copy();K.set_alpha(C);E.blit(K,(J,F));L=DD.get(H[T])
	if L:M=L.copy();M.set_alpha(C);E.blit(M,(J+220,F+52))
	if C>200 and A.time.get_ticks()//600%2==0:G=Ad.render('[ click anywhere to go back ]',P,(100,82,55));G.set_alpha(C);E.blit(G,(B//2-G.get_width()//2,F+652))
def Cc(surface,alpha):
	A=w.get(A4)
	if A:E=B-A.get_width()-10;F=D-200-A.get_height()+25;C=A.copy();C.set_alpha(alpha);surface.blit(C,(E,F))
C=B1;Bq=0;AF=0;Cd=0;An=0;Ao=0;Ce=0;Ap=0;DW=160;o=A.Surface((B,D));o.fill((0,0,0));BI=BS(B//2);AS=BS(-200);AT=R;p=-12.;Br=-6e1;Cf=N;Bs=1;Aq=N;Ar=N;BJ=K;Bt=K;Bu=N;As=0;Cg=0;At=0;DX=180;Au=N;BK=0;Bv=0;Bw=0;Av=0;Ch=600;Ci=B//2-300;BL=D//2+120;Bx=K;AG=A.Rect(B-120,20,100,32);f=K;q=M;BM='Are you sure you want to leave the case?';A0=K;Cj=K;Ck=K;A1=A.Rect(B//2-120,D//2+20,100,36);A2=A.Rect(B//2+20,D//2+20,100,36);BN=0;Cl=A.Rect(0,0,0,0);DY=A.time.Clock();By=F
while By:
	DY.tick(60);j=CT();Bx=AG.collidepoint(j);Cj=A1.collidepoint(j)if f else K;Ck=A2.collidepoint(j)if f else K
	for AU in A.event.get():
		if AU.type==A.QUIT:
			if C==u:f=F;q=M;A0=K
			else:By=K
		if AU.type==A.KEYDOWN:
			if AU.key==A.K_F11:
				Bh=not Bh
				if Bh:AK=A.display.set_mode((0,0),A.FULLSCREEN)
				else:AK=A.display.set_mode((1280,720),A.RESIZABLE)
			if AU.key==A.K_ESCAPE and C not in(B1,AW):
				f=not f
				if f:q=M;A0=K
		if AU.type==A.MOUSEBUTTONDOWN and AU.button==1:
			if f and A0:
				if A1.collidepoint(j):By=K
				if A2.collidepoint(j):f=K
			elif C==B5:BH=Z;AR=0;Bp=S;C=AZ
			elif C==AZ:
				DZ=Ca();BO=Z
				for(Da,Db,Dc)in DZ:
					if A.Rect(Db-10,Dc-8,240,42).collidepoint(j):BO=Da;break
				if BO:BH=next(A for A in CQ if A[T]==BO);Am.add(BO);AR=0;Bp=P;C=B5
				elif I(Am)==5:AP=BZ;n=0;AD=A3;Al=M;AE=S;CW=S;z=0;C=AY
			elif C==AY:
				if not Aj:Aj=P;BG=CU
				elif AP==BZ:
					if not AE:AD=I(AA[n][1]);Al=AA[n][1];AE=P
					else:
						n+=1
						if n<I(AA):Al=M;AD=A3;AE=S
						else:CW=P;C=B4b;act3t=0
				elif not AC:AB=I(A9[m][1]);Ak=A9[m][1];AC=P
				else:
					m+=1
					if m<I(A9):Ak=M;AB=A3;AC=S
					else:CV=P;i=0;AQ=D;DT=S;C=AZ
			elif C==u and Bx:BE='A';d=I(CR);C=Ab;Ag=0;A7=0;A8=N;AM=K;AN=[];AO=M
			elif C==Ab:
				if not AM:AN=[A for(B,A)in Ah];A7=I(Ah);AM=F
				else:BE='B';d=0;Af=M;A5=N;A6=K;C=u
			elif C==u and not f:
				r=BF()
				if not A6:A5=I(r[d][1]);Af=r[d][1];A6=F
				else:
					d+=1
					if d<I(r):Af=M;A5=N;A6=K
					elif BE=='A':C=Ab;Ag=0;A7=0;A8=N;AM=K;AN=[];AO=M
					else:BN=0;C=B4
			elif C==B4 and BN>65:
				if A.Rect(B//2-110,D//2+78,220,48).collidepoint(j):C=AY;DS=0;m=0;AB=A3;Ak=M;AC=S;CV=S;z=0;AP=C8
			elif C==B4b and act3t>65:
				if A.Rect(B//2-110,D//2+78,220,48).collidepoint(j):By=K
			elif C==AW and Cl.collidepoint(j):C=Be;Bq=15
			elif C==Aa and BJ and not Bt:C=Bd
	if C==B1:
		if An<255:An=H(255,An+2)
		elif Ao<255:Ao=H(255,Ao+2)
		elif Ce<DW:Ce+=1
		else:
			Ap=H(255,Ap+4)
			if Ap>=255:C=AW
	elif C==Be:
		Bq=Y(N,Bq-.2);AF=H(255,AF+2);Cd=H(R,Cd+.03)
		if AF>=255:C=Bc
	elif C==Bc:
		Cf+=.3;AS+=Cf;Br+=Bs*.4
		if abs(Br)>55:Bs*=-1
		p+=Bs*.08;p=Y(-14.,H(14.,p));BI=B//2+Br
		if AS>=D//2:AS=BS(D//2);BI=BS(B//2);Ar=p*.4;C=Bb
	elif C==Bb:
		Ar+=-Aq*.25;Ar*=.78;Aq+=Ar;p=Aq
		if abs(Aq)<.1 and abs(Ar)<.05:p=N;Aq=N;C=Aa
	elif C==Aa:p=N;Dd=A.Rect(G(BI)-Bj//2,G(AS)-BA//2,Bj,BA);BJ=Dd.collidepoint(j);AT+=((1.07 if BJ else R)-AT)*.15
	elif C==Bd:
		Bu=H(R,Bu+.02);AT+=(1.05-AT)*.08
		if Bu>=R:Bt=F;C=B2
	elif C==B2:
		As=H(255,As+3)
		if As>=255:C=AX
	elif C==AX:
		Cg+=1
		if Cg>=DX:
			At=H(255,At+3)
			if At>=255:C=Ba
	elif C==Ba:
		if BK<255:BK=H(255,BK+3)
		if Au<R:Au=H(R,Au+.004)
		Bv+=1
		if Bv>=20:Bv=0;Bw=(Bw+1)%3
		if Au>=R:
			Av=H(255,Av+3)
			if Av>=255:C=u;BC=0;h=N;BB=K
	elif C==Ab:
		Ag=H(255,Ag+4)
		if A7<I(Ah):
			De,s=Ah[A7]
			if De in(Bf,AJ):AN.append(s);A7+=1;AO=M
			else:
				A8=H(I(s),A8+DK);AO=s[:G(A8)]
				if A8>=I(s):AN.append(s);A7+=1;A8=N;AO=M
		else:AM=F
	elif C==u:
		Bl=H(255,Bl+4);r=BF()
		if BC<CN:BC+=1
		if d<I(r)and not A6:
			s=r[d][1];A5=H(I(s),A5+Bm);Af=s[:G(A5)]
			if A5>=I(s):A6=F
		if f and not A0:
			if I(q)<I(BM):q=BM[:I(q)+1]
			else:A0=F
	if f and not A0 and C not in(u,):
		if I(q)<I(BM):q=BM[:I(q)+1]
		else:A0=F
	elif C==B4:BN+=1
	elif C==B4b:act3t+=1
	elif C==AY:
		if Ai<255:Ai=H(255,Ai+3)
		if not Aj:
			BG+=1
			if BG>=CU:Aj=P
		else:
			z=H(255,z+4)
			if AP==BZ:
				if n<I(AA)and not AE:
					AH=AA[n][1];AD=H(I(AH),AD+Bm);Al=AH[:G(AD)]
					if AD>=I(AH):AE=P
			elif m<I(A9)and not AC:
				AH=A9[m][1];AB=H(I(AH),AB+Bm);Ak=AH[:G(AB)]
				if AB>=I(AH):AC=P
	elif C==AZ:
		if i<255:i=H(255,i+3)
		if AQ>CX:AQ=Y(CX,AQ-12)
	elif C==B5:
		if Bp and AR<255:AR=H(255,AR+8)
	E.fill(C_)
	if C==B1:
		if l and An>0:Cm=l.copy();Cm.set_alpha(An);E.blit(Cm,((B-l.get_width())//2,(D-l.get_height())//2-30))
		if Ao>0:Bz=D1.render('WARNING: This game contains lies, manipulation, and birthday wishes.',F,CD);Bz.set_alpha(Ao);Df=D//2+l.get_height()//2+10 if l else D//2+260;E.blit(Bz,(B//2-Bz.get_width()//2,Df))
		if Ap>0:o.set_alpha(Ap);E.blit(o,(0,0))
	if C in(AW,Be):
		E.fill((4,3,2))
		for X in CO:
			Cn=A.Surface((X[b]*2,X[b]*2),A.SRCALPHA);A.draw.circle(Cn,(155,138,105,X[B3]),(X[b],X[b]),X[b]);E.blit(Cn,(X[g],X[c]));X[c]-=X['speed']
			if X[c]<-20:X[c]=D+20;X[g]=U.randint(0,B)
		DI(E)
		if l:Dg=math.sin(A.time.get_ticks()*.0008)*4;E.blit(l,((B-l.get_width())//2,80+Dg))
		if AF<200:Cl=DJ(E,1.,j,C,AF)
		if AF>0:o.set_alpha(G(AF));E.blit(o,(0,0))
	if C in(Bc,Bb,Aa,Bd,B2,AX):
		if CI:
			BP=G(Bj*AT);BQ=G(BA*AT);Aw=A.transform.smoothscale(CI,(BP,BQ))
			if p!=N:Aw=A.transform.rotozoom(Aw,-p,R)
			E.blit(Aw,(G(BI)-Aw.get_width()//2,G(AS)-Aw.get_height()//2))
		if BJ and not Bt and C==Aa:Co=Ad.render('[ click to open ]',F,CD);E.blit(Co,(B//2-Co.get_width()//2,G(AS)+BA//2+18))
	if C in(B2,AX)and As>0:DR(E,As)
	if C==AX and At>0:o.set_alpha(At);E.blit(o,(0,0))
	if C==Ba:
		DN(E,BK,Au,Bw)
		if Av>0:o.set_alpha(Av);E.blit(o,(0,0))
	if C==u:
		if CK:E.blit(CK,(0,0));DH(E)
		else:E.fill((18,14,10))
		r=BF()
		if d<I(r):
			Dh,Dz,Di=r[d]
			if Dh==Q and BC>=CN:
				BB=F;h=H(R,h+.03);Bn(Di);Bo();t=w.get(A4)
				if t:Dj=G(255*h*e);B_=B-t.get_width()-10;C0=D-200-t.get_height()+25;Ax=t.copy();Ax.set_alpha(Dj);E.blit(Ax,(B_,C0))
			elif BB:
				h=Y(N,h-.03)
				if h<=0:BB=K
				if h>0:
					t=w.get(A4)
					if t:B_=B-t.get_width()-10;C0=D-200-t.get_height()+25;Ax=t.copy();Ax.set_alpha(G(255*h));E.blit(Ax,(B_,C0))
		DO(E,Bl);DP(E,Bx)
	if C==Ab:E.fill((12,9,6));DL(E,Ag,AN,AO,AM)
	if C==B4:DM(E,BN)
	if C==B4b:act3_draw(E,act3t)
	if C==AY:
		if AL:E.blit(AL,(0,0))
		else:E.fill((8,6,4))
		if Ai<255:C1=A.Surface((B,D));C1.fill((0,0,0));C1.set_alpha(255-Ai);E.blit(C1,(0,0))
		if not Aj:C2=H(255,BG*4);Ay,Az=520,90;C3=A.Surface((Ay,Az),A.SRCALPHA);C3.fill((0,0,0,180));C3.set_alpha(C2);E.blit(C3,(B//2-Ay//2,D//2-Az//2-10));Cp=A.Surface((Ay,Az),A.SRCALPHA);A.draw.rect(Cp,(100,80,50,C2),(0,0,Ay,Az),1);E.blit(Cp,(B//2-Ay//2,D//2-Az//2-10));C4=D3.render('The Bus  —  10:15 PM',P,(210,195,165));C4.set_alpha(C2);E.blit(C4,(B//2-C4.get_width()//2,D//2-24))
		elif AP==C8 and m<I(A9):
			A_,Dk,C5=A9[m]
			if A_==C6:Bn(C5);Bo();Cc(E,z)
			CZ(E,z,Ak,A_,AC)
		elif AP==BZ and n<I(AA):
			A_,Dk,C5=AA[n]
			if A_==C6:Bn(C5);Bo();Cc(E,z)
			CZ(E,z,Al,A_,AE)
	if C==AZ:Cb(E)
	if C==B5 and BH:
		if AL:E.blit(AL,(0,0))
		else:E.fill((8,6,4))
		Cb(E);Cq=A.Surface((B,D),A.SRCALPHA);Cq.fill((0,0,0,160));E.blit(Cq,(0,0));DV(E,BH,AR)
	if f:DQ(E,q,A0,Cj,Ck)
	BP,BQ=AK.get_size();Cr=H(BP/B,BQ/D);Cs,Ct=G(B*Cr),G(D*Cr);Dl=A.transform.smoothscale(E,(Cs,Ct));AK.fill((0,0,0));AK.blit(Dl,((BP-Cs)//2,(BQ-Ct)//2));A.display.flip()
A.quit();sys.exit()
