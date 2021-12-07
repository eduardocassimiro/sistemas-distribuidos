/*
   Curso de Arduino e AVR 108
   
   WR Kits Channel


   Filtro de Média Móvel e Serial Plotter

    
   Autor: Eng. Wagner Rambo  Data: Março de 2017
   
   www.wrkits.com.br | facebook.com/wrkits | youtube.com/user/canalwrkits
   
*/


// ===============================================================================
// --- Mapeamento de Hardware ---
#define    pot     A0         //potenciômetro na entrada analógica 0


// ===============================================================================
// --- Constantes Auxiliares ---
#define      n     50        //número de pontos da média móvel 


// ===============================================================================
// --- Protótipo da Função ---
long moving_average();       //Função para filtro de média móvel


// ===============================================================================
// --- Variáveis Globais ---
int       original,          //recebe o valor de AN0
          filtrado;          //recebe o valor original filtrado

int       numbers[n];        //vetor com os valores para média móvel



// ===============================================================================
// --- Configurações Iniciais ---
void setup()
{
   Serial.begin(9600);    //serial inicia em 9600 baud rate
   pinMode(pot, INPUT);   //configura entrada para potenciômetro
 
  
} //end setup


// ===============================================================================
// --- Loop Infinito ---
void loop()
{
  
   original = analogRead(pot);

   filtrado = moving_average();

   //Serial.print(original);
   //Serial.print(" ");
   Serial.println(filtrado);


   delay(30);
  
  
} //end loop



// ===============================================================================
// --- Desenvolvimento da Função ---
long moving_average()
{

   //desloca os elementos do vetor de média móvel
   for(int i= n-1; i>0; i--) numbers[i] = numbers[i-1];

   numbers[0] = original; //posição inicial do vetor recebe a leitura original

   long acc = 0;          //acumulador para somar os pontos da média móvel

   for(int i=0; i<n; i++) acc += numbers[i]; //faz a somatória do número de pontos


   return acc/n;  //retorna a média móvel

 
} //end moving_average
