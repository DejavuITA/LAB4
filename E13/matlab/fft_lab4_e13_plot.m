function fft_output_value = fft_lab4_e13_plot( valori , freq, punti)
    fft_output_value= abs(fft(valori));
    frequenze=1:freq/punti:freq;
    figure();
    hold on;
    loglog(frequenze,fft_output_value);
    grid on;
end

