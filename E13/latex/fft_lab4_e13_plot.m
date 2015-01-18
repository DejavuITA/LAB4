function fft_output_value = fft_lab4_e13_plot( valori , tempo, freq, punti)
    fft_output_value= abs(fft(valori));
    temp=tempo(1);
    norma=0;
    for i=1:1:length(tempo)
        tempo(i)=tempo(i)-temp;
        norma=norma+fft_output_value(i);
    end
    frequenze=1:freq/punti:freq;
    figure();
    subplot(2,1,1);
    plot(tempo,valori);
    hold on
    grid on
    
    yl = ylabel('Tensione [V]');
	set(yl, 'FontSize', 32);
    
    xl = xlabel(['Tempo [s]']);
    set(xl, 'FontSize', 32);
    
    set(gca,'FontSize',32);
    
    subplot(2,1,2);
    loglog(frequenze(2:punti),fft_output_value(2:punti)/norma);
    hold on
    grid on
    
    yl = ylabel('Ampiezza [V/Hz]');
    set(yl, 'FontSize', 32);
    
    xl = xlabel(['Frequenza [Hz]']);
    set(xl, 'FontSize', 32);
    
    set(gca,'FontSize',32);
end