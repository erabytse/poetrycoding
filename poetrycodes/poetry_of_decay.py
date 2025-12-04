import time
import sys

class Nature:
    def __init__(self):
        self.mountains = "silent, ancient, breathing"
        self.rivers = "clear, singing, endless"
        self.forests = "deep, whispering, whole"
        self.balance = True
        self.memory = "alive"

    def status(self):
        if self.balance:
            return (
                f"🌿 Mountains: {self.mountains}\n"
                f"💧 Rivers:  {self.rivers}\n"
                f"🌳 Forests: {self.forests}\n"
                f"⚖️  Balance: held\n"
            )
        else:
            return (
                f"🌫️  Mountains: eroded, hollow\n"
                f"☠️  Rivers:  choked, silent\n"
                f"🪵 Forests: ash, memory\n"
                f"⚖️  Balance: lost\n"
            )

    def degrade(self, cause="forgetting"):
        """The slow unraveling."""
        self.mountains = "eroded, hollow"
        self.rivers = "choked, silent"
        self.forests = "ash, memory"
        self.balance = False
        self.memory = cause


class Human:
    def __init__(self, name="you or me"):
        self.name = name
        self.action = "to forget"

    def touch(self, nature):
        """The paradox: to care is to harm, to ignore is to destroy."""
        print(f"\n👣 {self.name} walks. Not with malice — only absence.")
        time.sleep(1.2)
        print("   He does not see the roots beneath his feet.")
        time.sleep(1.0)
        print("   He does not hear the river’s plea.")
        time.sleep(1.3)
        print("   He builds a world that forgets it is part of another.")
        time.sleep(1.5)
        nature.degrade(cause="the fragility of man")
        print("\n💔 The system exhales... and begins to crumble.")


# ——— PoetryCoding™ execution ———

if __name__ == "__main__":
    world = Nature()
    print("🌍 Initializing world...\n")
    print(world.status())
    time.sleep(2)

    man = Human()
    man.touch(world)

    time.sleep(1.8)
    print("\n" + "="*40)
    print("Final state of the world:")
    print("="*40)
    print(world.status())

    print("📜 Commit message:")
    print('chore(nature): the most fragile creature — man —')
    print('has written his name in ash upon the mountains.')
    print('')
    print('Not with fire.')
    print('Not with steel.')
    print('But with forgetting.')
    print('')
    print('This commit remembers.')