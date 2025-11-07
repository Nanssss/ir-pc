#include <IRremote.h>

int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);

decode_results results;
String msg ;

void setup()
{
    Serial.begin(9600);
    irrecv.enableIRIn(); // Start the receiver
}

void loop() {
    if (irrecv.decode(&results)) {
    
    switch(results.value) {
        // Here, map your IR hexa codes to their correponding commands
        case 0x9e0e10ff: msg = "FUP"          ; break;
        case 0x20DF40BF: msg = "FUP"          ; break;
        case 0x20DFC03F: msg = "FDOWN"        ; break;
        case 0x8EEF4B83: msg = "FDOWN"        ; break;
        case 0xB4B44CB3: msg = "FLEFT"        ; break;
        case 0x51CEC000: msg = "FLEFT"        ; break;
        case 0xB4B4CC33: msg = "FRIGHT"       ; break;
        case 0xD380803A: msg = "FRIGHT"       ; break;
        case 0x6AF21320: msg = "OK"           ; break;
        case 0xB4B41AE5: msg = "OK"           ; break;
        case 0xB4B4A25D: msg = "RETURN"       ; break;
        case 0xA4F68FBE: msg = "RETURN"       ; break;
        case 0xB4B45CA3: msg = "DISPLAY"      ; break;
        case 0x597B1824: msg = "DISPLAY"      ; break;
        case 0xB4B452AD: msg = "TITLE"        ; break;
        case 0x1018FF80: msg = "TITLE"        ; break;
        case 0xB4B4E21D: msg = "UP"           ; break;
        case 0x9986485A: msg = "UP"           ; break;
        case 0xB4B412ED: msg = "DOWN"         ; break;
        case 0x1C6A919C: msg = "DOWN"         ; break;
        case 0xB4B49A65: msg = "LEFT"         ; break;
        case 0x4EBA0422: msg = "LEFT"         ; break;
        case 0xB4B45AA5: msg = "RIGHT"        ; break;
        case 0x5EA08104: msg = "RIGHT"        ; break;
        case 0x20DF00FF: msg = "MUP"          ; break;
        case 0x86288A23: msg = "MUP"          ; break;
        case 0x20DF807F: msg = "MDOWN"        ; break;
        case 0x169CDC1F: msg = "MDOWN"        ; break;
        case 0xB4B49C63: msg = "STOP"         ; break;
        case 0xCA9582FA: msg = "STOP"         ; break;
        case 0xB4B42CD3: msg = "SKIP"         ; break;
        case 0x1E6BA628: msg = "SKIP"         ; break;
        case 0xB4B46C93: msg = "ENTER"        ; break;
        case 0x645DD5C4: msg = "ENTER"        ; break;
        case 0xC2E92AD6: msg = "PLAY"         ; break;
        case 0xB4B48C73: msg = "PLAY"         ; break;
        case 0xB4B40CF3: msg = "POWER"        ; break;
        case 0xB595064 : msg = "POWER"        ; break;
        case 0xB4B4D22D: msg = "MENU"         ; break;
        case 0x9BED8042: msg = "MENU"         ; break;
        case 0xB4B41CE3: msg = "PAUSE"        ; break;
        case 0x22CF7E40: msg = "PAUSE"        ; break;
        case 0xB4B4DC23: msg = "1"            ; break;
        case 0xDB2CD85E: msg = "1"            ; break;
        case 0xB4B43CC3: msg = "2"            ; break;
        case 0x72C8CD04: msg = "2"            ; break;
        case 0xB4B4BC43: msg = "3"            ; break;
        case 0xBFA12A36: msg = "3"            ; break;
        case 0xB4B446B9: msg = "SEARCH"       ; break;
        case 0x82A4D940: msg = "SEARCH"       ; break;
        default:         msg = "NONE" ;       ; break;
    }
    
    if (msg != "NONE") {
        Serial.println(msg);
    }

    irrecv.resume(); // Receive the next value
    }      
}
