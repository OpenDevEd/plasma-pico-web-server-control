import plasma_config 
import plasma_fire
import plasma_rainbows

async def run_plasma_pattern():
    # Stay in this function, until the pattern state is changed
    print("Running pattern "+str(plasma_config.state))
    plasma_config.running = 1
    if plasma_config.state==1:
        await plasma_fire.fire()
    elif plasma_config.state==2:
        await plasma_rainbows.rainbows()
    else:
        print("No pattern defined.")
    plasma_config.running = 0
    print("Done with led_pattern selection")

#set_led_pattern(1)
#run_led_pattern()