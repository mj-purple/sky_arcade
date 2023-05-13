import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { JuegoPiedraPapelTijerasComponent } from './juego-piedra-papel-tijeras/juego-piedra-papel-tijeras.component';
import { RPSComponent } from './games/rps/rps.component';
import { JuegoPiedraPapelTijeraComponent } from './games/juego-piedra-papel-tijera/juego-piedra-papel-tijera.component';

@NgModule({
  declarations: [
    AppComponent,
    JuegoPiedraPapelTijerasComponent,
    RPSComponent,
    JuegoPiedraPapelTijeraComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
