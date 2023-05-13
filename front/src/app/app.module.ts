import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { JuegoPiedraPapelTijeraComponent } from './games/juego-piedra-papel-tijera/juego-piedra-papel-tijera.component';
import { DecoratorsTopBotComponent } from './decorators-top-bot/decorators-top-bot.component';

@NgModule({
  declarations: [
    AppComponent,
    DecoratorsTopBotComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
