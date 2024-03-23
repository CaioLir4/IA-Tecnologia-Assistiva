const int botaoPin = 2; // Qual o pino
int LedA1 = 13; // Porta dos LEDs de cima
int LedA2 = 12;
int LedA3 = 11;
int LedB1 = 10; // Porta dos LEDs de baixo
int LedB2 = 9;
int LedB3 = 8;

int delayInputs = 1000;
void setup() {
  Serial.begin(9600);
  // GPT -> "Configura o pino do botão como entrada com pull-up interno"
  pinMode(LedA1, OUTPUT);
  pinMode(LedA2, OUTPUT);
  pinMode(LedA3, OUTPUT);
  pinMode(LedB1, OUTPUT);
  pinMode(LedB2, OUTPUT);
  pinMode(LedB3, OUTPUT);
}

void loop() {
   // Ver se o botão ta pressionado pra ler e identificar a letra
    char letra = lerLetra();
    identificarLetra(letra);
    delay(800); // Determina o quão rápido ocorre a identificação

}

char lerLetra() {
  Serial.println("Digite uma letra: ");
  while (!Serial.available()); // GPT -> "Aguarda até que algum dado esteja disponível na porta serial"
  return Serial.read(); // Manda pro identificarLetra
}

void identificarLetra(char letra) { // Lista de letras e gatilhos de eventos
  switch (letra) {

    case 'a':
    case 'A':
      Serial.println("A reconhecido");
      digitalWrite(LedA3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      break;

    case 'b':
    case 'B':
      Serial.println("B reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      break;

    case 'c':
    case 'C':
      Serial.println("C reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedB3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedB3, LOW);
      break;

    case 'd':
    case 'D':
      Serial.println("D reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'e':
    case 'E':
      Serial.println("E reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'f':
    case 'F':
      Serial.println("F reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedB3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedB3, LOW);
      break;

    case 'g':
    case 'G':
      Serial.println("G reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'h':
    case 'H':
      Serial.println("H reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'i':
    case 'I':
      Serial.println("I reconhecido");
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedB3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedB3, LOW);
      break;

    case 'j':
    case 'J':
      Serial.println("J reconhecido");
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'k':
    case 'K':
      Serial.println("K reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      break;

    case 'l':
    case 'L':
      Serial.println("L reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      break;

    case 'm':
    case 'M':
      Serial.println("M reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      break;

    case 'n':
    case 'N':
      Serial.println("N reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'o':
    case 'O':
      Serial.println("O reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'p':
    case 'P':
      Serial.println("P reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      break;

    case 'q':
    case 'Q':
      Serial.println("Q reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'r':
    case 'R':
      Serial.println("R reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 's':
    case 'S':
      Serial.println("S reconhecido");
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      delay(delayInputs);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      break;

    case 't':
    case 'T':
      Serial.println("T reconhecido");
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      delay(delayInputs);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      break;

    case 'u':
    case 'U':
      Serial.println("U reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB1, LOW);
      break;

    case 'v':
    case 'V':
      Serial.println("V reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB1, LOW);
      break;

    case 'w':
    case 'W':
      Serial.println("W reconhecido");
      digitalWrite(LedA2, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      digitalWrite(LedB1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA2, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      digitalWrite(LedB1, LOW);
      break;

    case 'x':
    case 'X':
      Serial.println("X reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB1, LOW);
      break;

    case 'y':
    case 'Y':
      Serial.println("Y reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB3, HIGH);
      digitalWrite(LedB2, HIGH);
      digitalWrite(LedB1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB3, LOW);
      digitalWrite(LedB2, LOW);
      digitalWrite(LedB1, LOW);
      break;

    case 'z':
    case 'Z':
      Serial.println("Z reconhecido");
      digitalWrite(LedA3, HIGH);
      digitalWrite(LedA1, HIGH);
      digitalWrite(LedB2, HIGH);
      digitalWrite(LedB1, HIGH);
      delay(delayInputs);
      digitalWrite(LedA3, LOW);
      digitalWrite(LedA1, LOW);
      digitalWrite(LedB2, LOW);
      digitalWrite(LedB1, LOW);
      break;

    default:
      Serial.println("Letra irreconhecida.");
  }
}
