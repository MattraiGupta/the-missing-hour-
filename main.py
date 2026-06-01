_n='CASE FILE NO. 17-4'
_m='header'
_l='glitch'
_k='loading'
_j='envelope_wobble'
_i='envelope_fly'
_h='envelope_opening'
_g='transition'
_f='tbc'
_e='intro'
_d='divider'
_c='focused'
_b='worried'
_a='surprised'
_Z='Georgia'
_Y='letter_reveal'
_X='menu'
_W='puzzle'
_V='alpha'
_U='side'
_T='letter_hold'
_S='chapter2_ready'
_R='envelope_idle'
_Q='casefile'
_P='label'
_O='spacer'
_N='reading'
_M='gameplay'
_L='x'
_K='size'
_J='y'
_I='body'
_H=None
_G='Courier New'
_F=1.
_E='neutral'
_D='Diya'
_C=.0
_B=False
_A=True
import pygame,sys,os,random,math
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=1280,720
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('The Missing Hour')
BG_BLACK=0,0,0
STARK_WHITE=245,245,245
MUTED_GRAY=120,120,120
PARCHMENT=240,228,196
INK_DARK=40,30,20
start_font=pygame.font.SysFont(_G,28,bold=_A)
hint_font=pygame.font.SysFont(_G,16)
warning_font=pygame.font.SysFont(_G,15)
loading_font=pygame.font.SysFont(_G,16)
location_font=pygame.font.SysFont(_Z,48)
time_font=pygame.font.SysFont(_G,20)
casefile_font=pygame.font.SysFont(_G,16)
dialogue_font=pygame.font.SysFont(_Z,26)
name_font=pygame.font.SysFont(_G,16,bold=_A)
skip_font=pygame.font.SysFont(_G,13)
exit_font=pygame.font.SysFont(_G,18)
exit_big_font=pygame.font.SysFont(_Z,22)
cf_title_font=pygame.font.SysFont(_G,20,bold=_A)
cf_body_font=pygame.font.SysFont(_G,19)
cf_label_font=pygame.font.SysFont(_G,16,bold=_A)
cf_stamp_font=pygame.font.SysFont(_G,48,bold=_A)
frag_font=pygame.font.SysFont(_G,13)
current_folder=os.path.dirname(os.path.abspath(__file__))
def load_img(filename,size=_H,alpha=_B):
	A=filename
	try:C='convert_alpha'if alpha else'convert';B=getattr(pygame.image.load(os.path.join(current_folder,A)),C)();return pygame.transform.smoothscale(B,size)if size else B
	except Exception as D:print(f"Could not load {A}: {D}");return
logo_img=load_img('logo.png',(480,480))
env_img=load_img('env.png',(900,375))
letter_img=load_img('letter.png',(480,570))
office_img=load_img('office.png',(1280,720))
dialogbox_img=load_img('dialogue_box.png',(1280,200),alpha=_A)
ENV_W,ENV_H=900,375
MAX_CHAR_HEIGHT=320
def load_expr(f):
	try:
		A=pygame.image.load(os.path.join(current_folder,f)).convert_alpha()
		if A.get_height()>MAX_CHAR_HEIGHT:B=MAX_CHAR_HEIGHT/A.get_height();A=pygame.transform.smoothscale(A,(int(A.get_width()*B),MAX_CHAR_HEIGHT))
		return A
	except:return
DIYA={}
for expr in[_E,'angry','sad','smug','smiling','soft','tired',_a]:DIYA[expr]=load_expr(f"diya_{expr}.png")
for(e,img)in DIYA.items():
	if not img:DIYA[e]=DIYA[_E]
diya_visible=_B
diya_fade=_C
diya_entrance_delay=0
DIYA_ENTRANCE_FRAMES=90
current_expr=_E
target_expr=_E
expr_fade=_F
menu_btn_scale=_F
menu_pulse=.008
menu_particles=[]
for _ in range(50):menu_particles.append({_L:random.randint(0,SCREEN_WIDTH),_J:random.randint(0,SCREEN_HEIGHT),'speed':random.uniform(.2,1.0),_K:random.randint(1,2),_V:random.randint(30,90)})
office_particles=[]
for _ in range(60):office_particles.append({_L:random.randint(0,SCREEN_WIDTH),_J:random.randint(0,SCREEN_HEIGHT),'sx':random.uniform(-.3,.3),'sy':random.uniform(.1,.5),_K:random.randint(1,2),_V:random.randint(20,60)})
ambient_flicker=0
flicker_timer=0
_rng=random.Random(42)
NOIR_FRAGS=[
	('CASE #17-4',_rng.randint(60,400),_rng.randint(60,160),_rng.randint(-18,18)),
	('MISSING',_rng.randint(500,900),_rng.randint(80,200),_rng.randint(-12,12)),
	('08:47 PM',_rng.randint(900,1180),_rng.randint(60,180),_rng.randint(-20,20)),
	('NO WITNESSES',_rng.randint(40,300),_rng.randint(500,640),_rng.randint(-15,15)),
	('[CLASSIFIED]',_rng.randint(700,1100),_rng.randint(480,640),_rng.randint(-22,22)),
	('THE GILT ROOM',_rng.randint(300,700),_rng.randint(560,680),_rng.randint(-10,10)),
	('REDACTED',_rng.randint(100,400),_rng.randint(280,420),_rng.randint(-25,25)),
	('11PM - MIDNIGHT',_rng.randint(750,1150),_rng.randint(300,440),_rng.randint(-14,14)),
]

DIALOGUE_A=[
	(_H,'The office smells like cold coffee and old paper.', _E),
	(_H,'The clock on the wall reads 08:47 PM.', 'tired'),
	(_D,'Okay. Coat. Keys. Door. We are leaving.', 'tired'),
	(_H,"She'd been saying that for forty minutes.", _E),
	(_H,'That\'s when she saw it. An envelope. Dark red wax seal. No return address.', _E),
	(_H,'Just three words written carefully across the front: FOR THE DETECTIVE.', _E),
	(_D,'...I don\'t see it.', 'tired'),
	(_H,'She saw it.', _E),
	(_H,'She stood there for a full thirty seconds. Then sat back down, still in her coat.', 'tired'),
	(_D,'One look. That\'s it.', 'tired'),
	(_H,'She told herself that too.', _E),
	(_H,'One page. Almost empty. Five witnesses. One missing hour.', _N),
	(_H,'Nobody remembers anything — word for word, every statement identical:', _N),
	(_H,'"I don\'t remember."', _N),
	(_D,'...That makes no sense.', _a),
	(_H,'She read it a third time.', _N),
	(_H,'She told herself she was just organizing. Not investigating. Just. Organizing.', _E),
	(_H,'The fifth folder disagreed.', _E),
]

DIALOGUE_B=[
	(_D,'Rayan Malik. Twenty-four. No signs of struggle. No explanation.', _N),
	(_H,'She closed the file. Opened it again.', _E),
	(_D,'I hate this job.', 'sad'),
	(_H,'She said it the way people say "I love this job."', _E),
	(_D,'Ameera, Mari, Insiya, Marwan, Neel.', _N),
	(_D,'One of them knows something.', 'smug'),
	(_H,'The office feels different now. Heavier.', _E),
	(_D,'What really happened at that party?', _b),
	(_H,'At some point she stopped arguing with herself and just put her coat on.', 'tired'),
	(_H,'The files came with her.', _E),
	(_H,'Obviously.', _E),
	(_H,'The office light clicked off behind her.', _E),
]

dialogue_part='A'
dialogue_idx=0
type_progress=_C
type_text=''
dialogue_done=_B
box_alpha=0
TYPEWRITER_SPEED=1.2
def current_dialogue():return DIALOGUE_A if dialogue_part=='A'else DIALOGUE_B
expr_phase='idle'
expr_out_alpha=_F
def set_expr(emotion):
	global current_expr,target_expr,expr_phase,expr_out_alpha
	B={'tired':'tired','reading':_N,'thinking':_U,'focused':_N,'worried':_b}
	A=B.get(emotion,emotion)
	if A not in DIYA:A=_E
	if target_expr!=A:
		target_expr=A
		if diya_fade<.05:current_expr=A;expr_phase='idle';expr_out_alpha=_F
		else:expr_phase='out'
def update_expr():
	global current_expr,target_expr,expr_phase,expr_out_alpha
	if expr_phase=='out':
		expr_out_alpha=max(_C,expr_out_alpha-.07)
		if expr_out_alpha<=_C:current_expr=target_expr;expr_phase='in';expr_out_alpha=_C
	elif expr_phase=='in':
		expr_out_alpha=min(_F,expr_out_alpha+.07)
		if expr_out_alpha>=_F:expr_phase='idle';expr_out_alpha=_F
def draw_atmosphere(surf):
	global ambient_flicker,flicker_timer
	for A in office_particles:
		C=pygame.Surface((A[_K]*2,A[_K]*2),pygame.SRCALPHA);pygame.draw.circle(C,(200,190,170,A[_V]),(A[_K],A[_K]),A[_K]);surf.blit(C,(int(A[_L]),int(A[_J])));A[_L]+=A['sx'];A[_J]+=A['sy']
		if A[_L]<-20:A[_L]=SCREEN_WIDTH+20
		if A[_L]>SCREEN_WIDTH+20:A[_L]=-20
		if A[_J]>SCREEN_HEIGHT:A[_J]=-20
		if A[_J]<-20:A[_J]=SCREEN_HEIGHT
	flicker_timer+=1
	if flicker_timer>random.randint(60,180):flicker_timer=0;ambient_flicker=random.randint(-15,5)
	else:ambient_flicker=max(0,ambient_flicker*.95)
	if ambient_flicker:
		B=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
		if ambient_flicker>0:B.fill((255,245,220,ambient_flicker))
		else:B.fill((0,0,0,-ambient_flicker))
		surf.blit(B,(0,0))
def draw_menu_noir_bg(surface):
	for sl in range(0,SCREEN_HEIGHT,3):
		sc=pygame.Surface((SCREEN_WIDTH,1),pygame.SRCALPHA);sc.fill((0,0,0,22));surface.blit(sc,(0,sl))
	vig=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
	for r in range(720,0,-16):
		intensity=min(255,max(0,int((720-r)*0.42)));pygame.draw.circle(vig,(0,0,0,intensity),(SCREEN_WIDTH//2,SCREEN_HEIGHT//2),r)
	surface.blit(vig,(0,0))
	streak=pygame.Surface((SCREEN_WIDTH,120),pygame.SRCALPHA)
	for sy in range(60):
		alpha=int(8*(1-abs(sy-30)/30));streak.fill((180,160,110,alpha),(0,sy,SCREEN_WIDTH,1))
	surface.blit(streak,(0,SCREEN_HEIGHT//2-60))

def draw_wax_seal_button(surface,scale,mouse_pos,game_state_val,darkness_val):
	bw=int(220*scale);bh=int(50*scale)
	bx=SCREEN_WIDTH//2-bw//2;by=596
	br=pygame.Rect(bx,by,bw,bh);mo=br.collidepoint(mouse_pos)
	if mo:pygame.draw.rect(surface,(18,14,8),br);pygame.draw.rect(surface,(255,255,255),br,2);tc=255,255,255
	else:pygame.draw.rect(surface,(8,6,3),br);pygame.draw.rect(surface,(200,200,200),br,1);tc=210,210,210
	st=start_font.render('START CASE',_A,tc)
	surface.blit(st,(bx+(bw-st.get_width())//2,by+(bh-st.get_height())//2))
	if game_state_val==_X:
		ha=80+math.sin(pygame.time.get_ticks()*.003)*40
		h=hint_font.render('[ click to begin your investigation ]',_A,(100,90,80))
		h.set_alpha(int(ha));surface.blit(h,(SCREEN_WIDTH//2-h.get_width()//2,by+bh+20))
	return br
case_alpha=0
case_line=0
case_char=_C
case_done=_B
CASEFILE_SPEED=1.5
CASEFILE=[(_m,_n),(_d,''),(_P,'SUBJECT'),(_I,'Rayan Malik, 24.'),(_O,''),(_P,'INCIDENT'),(_I,'Reported missing following a birthday gathering'),(_I,'at rooftop venue: The Gilt Room.'),(_I,'Last seen between 11 PM and midnight.'),(_O,''),(_P,'FINDINGS'),(_I,'No signs of struggle.'),(_I,'No witnesses.'),(_I,'No explanation.'),(_O,''),(_P,'WITNESS STATEMENTS  [x5]'),(_I,"Ameera  -  \"I don't remember.\""),(_I,"Mari    -  \"I don't remember.\""),(_I,"Insiya  -  \"I don't remember.\""),(_I,"Marwan  -  \"I don't remember.\""),(_I,"Neel    -  \"I don't remember.\""),(_O,''),('note','[ click to continue ]')]
case_revealed=[]
case_curr=''
def wrap_text(text,font,max_width):
	E=text.split(' ');B=[];A=''
	for C in E:
		D=A+(' 'if A else'')+C
		if font.size(D)[0]<=max_width:A=D
		else:
			if A:B.append(A)
			A=C
	if A:B.append(A)
	return B
def draw_casefile(surface,alpha,revealed,current_str,done):
	P=current_str;D=alpha;C=surface;G,H=820,620;I=SCREEN_WIDTH//2-G//2;M=SCREEN_HEIGHT//2-H//2
	J=pygame.Surface((G,H),pygame.SRCALPHA)
	J.fill((30,22,13,248))
	inner=pygame.Surface((G-20,H-20),pygame.SRCALPHA)
	inner.fill((38,28,16,60))
	J.blit(inner,(10,10))
	pygame.draw.rect(J,(115,90,52),(0,0,G,H),2)
	pygame.draw.rect(J,(75,60,35),(5,5,G-10,H-10),1)
	pygame.draw.rect(J,(55,42,24),(8,8,G-16,H-16),1)
	for(cx,cy) in[(14,14),(G-14,14),(14,H-14),(G-14,H-14)]:
		pygame.draw.circle(J,(100,78,44),(cx,cy),4,1)
	J.set_alpha(D);C.blit(J,(I,M));B=M+36;K=52;Q=revealed+([P]if P else[])
	for(R,(E,L))in enumerate(zip([A for(A,B)in CASEFILE],Q)):
		if E==_m:A=cf_title_font.render(L,_A,(185,158,112));A.set_alpha(D);C.blit(A,(SCREEN_WIDTH//2-A.get_width()//2,B));B+=36
		elif E==_d:N=pygame.Surface((G-K*2,1));N.fill((85,68,46));N.set_alpha(D);C.blit(N,(I+K,B));B+=20
		elif E==_P:
			bar=pygame.Surface((3,18),pygame.SRCALPHA);bar.fill((140,108,58,200));bar.set_alpha(D);C.blit(bar,(I+K-8,B+2))
			A=cf_label_font.render(L,_A,(148,118,72));A.set_alpha(D);C.blit(A,(I+K,B));B+=26
		elif E==_I:A=cf_body_font.render(L,_A,(215,200,170));A.set_alpha(D);C.blit(A,(I+K+16,B));B+=28
		elif E==_O:B+=14
		elif E=='note':
			if done and pygame.time.get_ticks()//500%2==0:A=cf_body_font.render(L,_A,(140,115,75));A.set_alpha(D);C.blit(A,(SCREEN_WIDTH//2-A.get_width()//2,B))
	if done:
		O=cf_stamp_font.render('UNSOLVED',_A,(140,40,40));O.set_alpha(min(D,175))
		F=O.get_rect(center=(SCREEN_WIDTH//2+180,M+H-80));C.blit(O,F)
		pygame.draw.rect(C,(140,40,40),(F.x-6,F.y-4,F.width+12,F.height+8),2)
		pygame.draw.rect(C,(100,25,25),(F.x-10,F.y-8,F.width+20,F.height+16),1)

def draw_chapter2_ready(surface,timer):
	B=timer;A=surface;A.fill((8,6,4));Y=int(B*1.4%(SCREEN_WIDTH+400))-200;Q=pygame.Surface((200,SCREEN_HEIGHT),pygame.SRCALPHA)
	for J in range(200):K=int(5*(1-abs(J-100)/100));pygame.draw.line(Q,(200,175,120,K),(J,0),(J,SCREEN_HEIGHT))
	A.blit(Q,(Y,0));R=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA)
	for S in range(600,0,-25):K=max(0,int((600-S)*.22));pygame.draw.circle(R,(0,0,0,K),(SCREEN_WIDTH//2,SCREEN_HEIGHT//2),S)
	A.blit(R,(0,0));E,F=SCREEN_WIDTH//2,SCREEN_HEIGHT//2
	for Z in[F-155,F+155]:T=pygame.Surface((560,1),pygame.SRCALPHA);T.fill((110,88,52,min(180,B*3)));A.blit(T,(E-280,Z))
	a=min(255,max(0,(B-10)*5));L=cf_label_font.render('C A S E  F I L E  -  A C T  T W O',_A,(120,95,58));L.set_alpha(a);A.blit(L,(E-L.get_width()//2,F-128))
	b=min(255,max(0,(B-25)*6));M=location_font.render('The Investigation Begins',_A,(210,195,165));M.set_alpha(b);A.blit(M,(E-M.get_width()//2,F-86))
	c=min(160,max(0,(B-40)*5));U=pygame.Surface((400,1),pygame.SRCALPHA);U.fill((100,80,50,c));A.blit(U,(E-200,F+20))
	d=min(255,max(0,(B-45)*5));N=casefile_font.render('The bus ride. Five witnesses. One missing hour.',_A,(100,88,68));N.set_alpha(d);A.blit(N,(E-N.get_width()//2,F+34))
	H=min(255,max(0,(B-65)*6));C,D=220,48;O,I=E-C//2,F+78;G=pygame.Surface((C,D),pygame.SRCALPHA);e=pygame.Rect(O,I,C,D).collidepoint(pygame.mouse.get_pos())
	if e:pygame.draw.rect(G,(60,50,35,220),(0,0,C,D),border_radius=3);pygame.draw.rect(G,(180,150,90,H),(0,0,C,D),2,border_radius=3);V=220,195,140
	else:pygame.draw.rect(G,(25,20,14,200),(0,0,C,D),border_radius=3);pygame.draw.rect(G,(100,82,52,H),(0,0,C,D),1,border_radius=3);V=150,128,90
	G.set_alpha(H);A.blit(G,(O,I));P=casefile_font.render('C O N T I N U E',_A,V);W=P.copy();W.set_alpha(H);A.blit(W,(O+C//2-P.get_width()//2,I+D//2-P.get_height()//2))

def draw_loading_screen(surface,alpha,bar_progress,dot_index):
	B=alpha;A=surface;C=SCREEN_WIDTH//2;E=casefile_font.render(_n,_A,(74,69,64));E.set_alpha(B);A.blit(E,(C-E.get_width()//2,190));D=pygame.Surface((500,1));D.fill((42,37,32));D.set_alpha(B);A.blit(D,(C-250,214));F=location_font.render('Downtown Office',_A,(200,191,176));F.set_alpha(B);A.blit(F,(C-F.get_width()//2,226));G=time_font.render('0 8 : 4 7   P M',_A,(90,82,72));G.set_alpha(B);A.blit(G,(C-G.get_width()//2,292));A.blit(D,(C-250,326));H=pygame.Surface((LOADING_BAR_W,2));H.fill((42,37,32));H.set_alpha(B);A.blit(H,(LOADING_BAR_X,LOADING_BAR_Y));K=int(LOADING_BAR_W*bar_progress)
	if K>0:I=pygame.Surface((K,2));I.fill((107,95,82));I.set_alpha(B);A.blit(I,(LOADING_BAR_X,LOADING_BAR_Y))
	L=[(58,53,48)]*3;L[dot_index]=107,95,82
	for(N,O)in enumerate(L):M=pygame.Surface((8,8),pygame.SRCALPHA);pygame.draw.circle(M,(*O,B),(4,4),4);A.blit(M,(C-20+N*20,LOADING_BAR_Y+22))
	J=loading_font.render('L O A D I N G . . .',_A,(58,53,48));J.set_alpha(B);A.blit(J,(C-J.get_width()//2,LOADING_BAR_Y+44))
def draw_dialogue_box(surface,alpha):
	C=alpha;B=surface;F=current_dialogue()
	if dialogue_idx>=len(F):return
	G=F[dialogue_idx][0];L,A,D=200,SCREEN_HEIGHT-200,28
	if dialogbox_img:H=dialogbox_img.copy();H.set_alpha(C);B.blit(H,(0,A))
	if G:I=name_font.render(G.upper(),_A,(180,155,110));I.set_alpha(C);B.blit(I,(D,A+8));J=A+52
	else:J=A+48
	for(M,N)in enumerate(wrap_text(type_text,dialogue_font,SCREEN_WIDTH-D*2)[:3]):K=dialogue_font.render(N,_A,(220,210,195));K.set_alpha(C);B.blit(K,(D,J+M*36))
	if dialogue_done and pygame.time.get_ticks()//500%2==0:E=hint_font.render('>',_A,(140,115,75));E.set_alpha(C);B.blit(E,(SCREEN_WIDTH-D-E.get_width(),A+L-28))
def draw_skip_button(surface,hovered):A=surface;C=(160,140,120)if hovered else(80,70,60);pygame.draw.rect(A,(12,10,8),SKIP_RECT);pygame.draw.rect(A,C,SKIP_RECT,1);B=skip_font.render('SKIP >>',_A,C);A.blit(B,(SKIP_RECT.x+(SKIP_RECT.width-B.get_width())//2,SKIP_RECT.y+(SKIP_RECT.height-B.get_height())//2))
def draw_exit_confirm(surface,typed_text,confirm_done,yes_hovered,no_hovered):
	A=surface;G=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SRCALPHA);G.fill((0,0,0,180));A.blit(G,(0,0));B,C=560,160;H,D=SCREEN_WIDTH//2-B//2,SCREEN_HEIGHT//2-C//2;pygame.draw.rect(A,(12,10,8),(H,D,B,C));pygame.draw.rect(A,(80,70,60),(H,D,B,C),1);I=exit_big_font.render(typed_text,_A,(200,190,175));A.blit(I,(SCREEN_WIDTH//2-I.get_width()//2,D+36))
	if confirm_done:J=(200,80,80)if yes_hovered else(120,60,60);K=(160,140,120)if no_hovered else(80,70,60);pygame.draw.rect(A,(12,10,8),EXIT_YES_RECT);pygame.draw.rect(A,J,EXIT_YES_RECT,1);E=exit_font.render('LEAVE',_A,J);A.blit(E,(EXIT_YES_RECT.x+(EXIT_YES_RECT.width-E.get_width())//2,EXIT_YES_RECT.y+(EXIT_YES_RECT.height-E.get_height())//2));pygame.draw.rect(A,(12,10,8),EXIT_NO_RECT);pygame.draw.rect(A,K,EXIT_NO_RECT,1);F=exit_font.render('STAY',_A,K);A.blit(F,(EXIT_NO_RECT.x+(EXIT_NO_RECT.width-F.get_width())//2,EXIT_NO_RECT.y+(EXIT_NO_RECT.height-F.get_height())//2))
def draw_letter(surface,alpha):
	if not letter_img:return
	A=letter_img.copy();A.set_alpha(alpha);surface.blit(A,(SCREEN_WIDTH//2-A.get_width()//2,SCREEN_HEIGHT//2-A.get_height()//2))

game_state=_e
shake=0
darkness=0
char_fade=0
intro_logo_alpha=0
intro_warn_alpha=0
intro_hold=0
intro_out=0
INTRO_HOLD=160
fade_surface=pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
fade_surface.fill((0,0,0))
env_x=float(SCREEN_WIDTH//2)
env_y=float(-200)
env_scale=_F
env_angle=-12.
env_drift=-6e1
env_vy=_C
drift_dir=1
wobble_angle=_C
wobble_vel=_C
env_hovered=_B
env_opened=_B
open_progress=_C
letter_alpha=0
letter_hold=0
letter_out=0
LETTER_HOLD_FRAMES=180
loading_progress=_C
loading_alpha=0
dot_timer=0
dot_idx=0
loading_out=0
LOADING_BAR_W=600
LOADING_BAR_X=SCREEN_WIDTH//2-300
LOADING_BAR_Y=SCREEN_HEIGHT//2+120
skip_hovered=_B
SKIP_RECT=pygame.Rect(SCREEN_WIDTH-120,20,100,32)
exit_confirm=_B
exit_type=''
EXIT_MESSAGE='Are you sure you want to leave the case?'
exit_done=_B
exit_yes_hover=_B
exit_no_hover=_B
EXIT_YES_RECT=pygame.Rect(SCREEN_WIDTH//2-120,SCREEN_HEIGHT//2+20,100,36)
EXIT_NO_RECT=pygame.Rect(SCREEN_WIDTH//2+20,SCREEN_HEIGHT//2+20,100,36)
ch2_anim_timer=0
button_rect=pygame.Rect(0,0,0,0)
clock=pygame.time.Clock()
running=_A
while running:
	clock.tick(60);mouse_pos=pygame.mouse.get_pos();skip_hovered=SKIP_RECT.collidepoint(mouse_pos);exit_yes_hover=EXIT_YES_RECT.collidepoint(mouse_pos)if exit_confirm else _B;exit_no_hover=EXIT_NO_RECT.collidepoint(mouse_pos)if exit_confirm else _B
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			if game_state==_M:exit_confirm=_A;exit_type='';exit_done=_B
			else:running=_B
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_ESCAPE and game_state not in(_e,_X):
				exit_confirm=not exit_confirm
				if exit_confirm:exit_type='';exit_done=_B
		if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
			if exit_confirm and exit_done:
				if EXIT_YES_RECT.collidepoint(mouse_pos):running=_B
				if EXIT_NO_RECT.collidepoint(mouse_pos):exit_confirm=_B
			elif game_state==_M and skip_hovered:dialogue_part='A';dialogue_idx=len(DIALOGUE_A);game_state=_Q;case_alpha=0;case_line=0;case_char=_C;case_done=_B;case_revealed=[];case_curr=''
			elif game_state==_Q:
				if not case_done:case_revealed=[A for(B,A)in CASEFILE];case_line=len(CASEFILE);case_done=_A
				else:dialogue_part='B';dialogue_idx=0;type_text='';type_progress=_C;dialogue_done=_B;game_state=_M
			elif game_state==_M and not exit_confirm:
				dl=current_dialogue()
				if not dialogue_done:type_progress=len(dl[dialogue_idx][1]);type_text=dl[dialogue_idx][1];dialogue_done=_A
				else:
					dialogue_idx+=1
					if dialogue_idx<len(dl):type_text='';type_progress=_C;dialogue_done=_B
					elif dialogue_part=='A':game_state=_Q;case_alpha=0;case_line=0;case_char=_C;case_done=_B;case_revealed=[];case_curr=''
					else:ch2_anim_timer=0;game_state=_S
			elif game_state==_S and ch2_anim_timer>65:
				if pygame.Rect(SCREEN_WIDTH//2-110,SCREEN_HEIGHT//2+78,220,48).collidepoint(mouse_pos):running=_B
			elif game_state==_X and button_rect.collidepoint(mouse_pos):game_state=_g;shake=15
			elif game_state==_R and env_hovered and not env_opened:game_state=_h
	if game_state==_e:
		if intro_logo_alpha<255:intro_logo_alpha=min(255,intro_logo_alpha+2)
		elif intro_warn_alpha<255:intro_warn_alpha=min(255,intro_warn_alpha+2)
		elif intro_hold<INTRO_HOLD:intro_hold+=1
		else:
			intro_out=min(255,intro_out+4)
			if intro_out>=255:game_state=_X
	elif game_state==_g:
		shake=max(_C,shake-.2);darkness=min(255,darkness+2);char_fade=min(_F,char_fade+.03)
		if darkness>=255:game_state=_i
	elif game_state==_i:
		env_vy+=.3;env_y+=env_vy;env_drift+=drift_dir*.4
		if abs(env_drift)>55:drift_dir*=-1
		env_angle+=drift_dir*.08;env_angle=max(-14.,min(14.,env_angle));env_x=SCREEN_WIDTH//2+env_drift
		if env_y>=SCREEN_HEIGHT//2:env_y=float(SCREEN_HEIGHT//2);env_x=float(SCREEN_WIDTH//2);wobble_vel=env_angle*.4;game_state=_j
	elif game_state==_j:
		wobble_vel+=-wobble_angle*.25;wobble_vel*=.78;wobble_angle+=wobble_vel;env_angle=wobble_angle
		if abs(wobble_angle)<.1 and abs(wobble_vel)<.05:env_angle=_C;wobble_angle=_C;game_state=_R
	elif game_state==_R:env_angle=_C;env_rect=pygame.Rect(int(env_x)-ENV_W//2,int(env_y)-ENV_H//2,ENV_W,ENV_H);env_hovered=env_rect.collidepoint(mouse_pos);env_scale+=((1.07 if env_hovered else _F)-env_scale)*.15
	elif game_state==_h:
		open_progress=min(_F,open_progress+.02);env_scale+=(1.05-env_scale)*.08
		if open_progress>=_F:env_opened=_A;game_state=_Y
	elif game_state==_Y:
		letter_alpha=min(255,letter_alpha+3)
		if letter_alpha>=255:game_state=_T
	elif game_state==_T:
		letter_hold+=1
		if letter_hold>=LETTER_HOLD_FRAMES:
			letter_out=min(255,letter_out+3)
			if letter_out>=255:game_state=_k
	elif game_state==_k:
		if loading_alpha<255:loading_alpha=min(255,loading_alpha+3)
		if loading_progress<_F:loading_progress=min(_F,loading_progress+.004)
		dot_timer+=1
		if dot_timer>=20:dot_timer=0;dot_idx=(dot_idx+1)%3
		if loading_progress>=_F:
			loading_out=min(255,loading_out+3)
			if loading_out>=255:game_state=_M;diya_entrance_delay=0;diya_fade=_C;diya_visible=_B
	elif game_state==_Q:
		case_alpha=min(255,case_alpha+4)
		if case_line<len(CASEFILE):
			kind,full_text=CASEFILE[case_line]
			if kind in(_d,_O):case_revealed.append(full_text);case_line+=1;case_curr=''
			else:
				case_char=min(len(full_text),case_char+CASEFILE_SPEED);case_curr=full_text[:int(case_char)]
				if case_char>=len(full_text):case_revealed.append(full_text);case_line+=1;case_char=_C;case_curr=''
		else:case_done=_A
	elif game_state==_M:
		box_alpha=min(255,box_alpha+4);dl=current_dialogue()
		if diya_entrance_delay<DIYA_ENTRANCE_FRAMES:diya_entrance_delay+=1
		if dialogue_idx<len(dl)and not dialogue_done:
			full_text=dl[dialogue_idx][1];type_progress=min(len(full_text),type_progress+TYPEWRITER_SPEED);type_text=full_text[:int(type_progress)]
			if type_progress>=len(full_text):dialogue_done=_A
		if exit_confirm and not exit_done:
			if len(exit_type)<len(EXIT_MESSAGE):exit_type=EXIT_MESSAGE[:len(exit_type)+1]
			else:exit_done=_A
	if exit_confirm and not exit_done and game_state not in(_M,):
		if len(exit_type)<len(EXIT_MESSAGE):exit_type=EXIT_MESSAGE[:len(exit_type)+1]
		else:exit_done=_A
	elif game_state==_S:ch2_anim_timer+=1
	screen.fill(BG_BLACK)
	if game_state==_e:
		if logo_img and intro_logo_alpha>0:lc=logo_img.copy();lc.set_alpha(intro_logo_alpha);screen.blit(lc,((SCREEN_WIDTH-logo_img.get_width())//2,(SCREEN_HEIGHT-logo_img.get_height())//2-30))
		if intro_warn_alpha>0:ws=warning_font.render('WARNING: This game contains lies, manipulation, and birthday wishes.',_A,MUTED_GRAY);ws.set_alpha(intro_warn_alpha);wy=SCREEN_HEIGHT//2+logo_img.get_height()//2+10 if logo_img else SCREEN_HEIGHT//2+260;screen.blit(ws,(SCREEN_WIDTH//2-ws.get_width()//2,wy))
		if intro_out>0:fade_surface.set_alpha(intro_out);screen.blit(fade_surface,(0,0))
	if game_state in(_X,_g):
		screen.fill((4,3,2))
		for p in menu_particles:
			ps=pygame.Surface((p[_K]*2,p[_K]*2),pygame.SRCALPHA);pygame.draw.circle(ps,(155,138,105,p[_V]),(p[_K],p[_K]),p[_K]);screen.blit(ps,(p[_L],p[_J]));p[_J]-=p['speed']
			if p[_J]<-20:p[_J]=SCREEN_HEIGHT+20;p[_L]=random.randint(0,SCREEN_WIDTH)
		draw_menu_noir_bg(screen)
		if logo_img:
			ly=math.sin(pygame.time.get_ticks()*.0008)*4
			screen.blit(logo_img,((SCREEN_WIDTH-logo_img.get_width())//2,80+ly))
		if darkness<200:
			button_rect=draw_wax_seal_button(screen,1.0,mouse_pos,game_state,darkness)
		if darkness>0:fade_surface.set_alpha(int(darkness));screen.blit(fade_surface,(0,0))
	if game_state in(_i,_j,_R,_h,_Y,_T):
		if env_img:
			sw=int(ENV_W*env_scale);sh=int(ENV_H*env_scale);scaled=pygame.transform.smoothscale(env_img,(sw,sh))
			if env_angle!=_C:scaled=pygame.transform.rotozoom(scaled,-env_angle,_F)
			screen.blit(scaled,(int(env_x)-scaled.get_width()//2,int(env_y)-scaled.get_height()//2))
		if env_hovered and not env_opened and game_state==_R:h=hint_font.render('[ click to open ]',_A,MUTED_GRAY);screen.blit(h,(SCREEN_WIDTH//2-h.get_width()//2,int(env_y)+ENV_H//2+18))
	if game_state in(_Y,_T)and letter_alpha>0:draw_letter(screen,letter_alpha)
	if game_state==_T and letter_out>0:fade_surface.set_alpha(letter_out);screen.blit(fade_surface,(0,0))
	if game_state==_k:
		draw_loading_screen(screen,loading_alpha,loading_progress,dot_idx)
		if loading_out>0:fade_surface.set_alpha(loading_out);screen.blit(fade_surface,(0,0))
	if game_state==_M:
		if office_img:screen.blit(office_img,(0,0));draw_atmosphere(screen)
		else:screen.fill((18,14,10))
		dl=current_dialogue()
		if dialogue_idx<len(dl):
			speaker,text,emotion=dl[dialogue_idx]
			if speaker==_D and diya_entrance_delay>=DIYA_ENTRANCE_FRAMES:
				diya_visible=_A;diya_fade=min(_F,diya_fade+.03);set_expr(emotion);update_expr()
				ci=DIYA.get(current_expr)
				if ci:
					final_alpha=int(255*diya_fade*expr_out_alpha)
					dx=SCREEN_WIDTH-ci.get_width()-10;dy=SCREEN_HEIGHT-200-ci.get_height()+25
					tmp=ci.copy();tmp.set_alpha(final_alpha);screen.blit(tmp,(dx,dy))
			elif diya_visible:
				diya_fade=max(_C,diya_fade-.03)
				if diya_fade<=0:diya_visible=_B
				if diya_fade>0:
					ci=DIYA.get(current_expr)
					if ci:dx=SCREEN_WIDTH-ci.get_width()-10;dy=SCREEN_HEIGHT-200-ci.get_height()+25;tmp=ci.copy();tmp.set_alpha(int(255*diya_fade));screen.blit(tmp,(dx,dy))
		draw_dialogue_box(screen,box_alpha);draw_skip_button(screen,skip_hovered)
	if game_state==_Q:screen.fill((12,9,6));draw_casefile(screen,case_alpha,case_revealed,case_curr,case_done)
	if game_state==_S:draw_chapter2_ready(screen,ch2_anim_timer)
	if exit_confirm:draw_exit_confirm(screen,exit_type,exit_done,exit_yes_hover,exit_no_hover)
	pygame.display.flip()
pygame.quit()
sys.exit()
